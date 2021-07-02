import time
import os, psutil
start_time = time.time()
def main():
    import pandas as pd
    header=['English','French']
    df=pd.read_csv('../french_dictionary.csv', names=header)
    data_dict = dict(zip(df.English, df.French))
    data_freq = dict.fromkeys(df.English, 0)
    eng=df['English']
    file1 = open('../t8.shakespeare.txt', 'r')
    text=file1.read()
    text=text.split(" ")
    transtext=""
    for word in text:
        if word in data_dict:
            transtext+=str(data_dict[word])+" "
            data_freq[word] += 1
        else:
            transtext+=str(word)+" "
    # print(transtext)
    # print(data_freq)
    output_data = pd.DataFrame(
        {'English word': list(df.English),
         'French word': list(df.French),
         'Frequency': list(data_freq.values())
         })
    filter_data= output_data[output_data.Frequency != 0]
    filter_data.to_csv(r'frequency.csv', index=False, header=True)
    file2 = open('../t8.shakespeare.translated.txt', 'w')
    file2.write(transtext)
    file2.close()
main()
print("--- %s seconds ---" % (time.time() - start_time))
process = psutil.Process(os.getpid())
print("--- %s bytes ---" % (process.memory_info().rss))