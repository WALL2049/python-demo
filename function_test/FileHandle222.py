import os

class FileHandle:
    def __init__(self):
        pass

    @staticmethod
    def write_result_to_file(file_path, file_name, result_keys, result_values):
        if not os.path.exists(file_path):
            # os.makedirs(file_path)
            os.mkdir(file_path)
        with open(file_path + "/" + file_name, "a") as file:
            for i in range(len(result_keys)):
                file.write(f"{result_keys[i]} = {result_values[i]}\n")


if __name__ == "__main__":

    resultKeys=["a","b","c","d"]
    resultValues=["1222","2","3","4"]
    filePath="D:/mts_auto/singlePCC"
    fileName="ping_result1.txt"
    # fileMethod.write_result_to_file(filePath, fileName, resultKeys, resultValues)
    FileHandle.write_result_to_file(filePath, fileName, resultKeys, resultValues)