import os
import validator
# Noa Azoulay


class GetFiles:
    @staticmethod
    # get list of all txt files paths in directory
    def get_list_of_files(path):
        files_list = []
        # r=root, d=directories, f=files
        for r, d, f in os.walk(path):
            for file in f:
                if '.txt' in file:
                    files_list.append(os.path.join(r, file).replace(os.sep, '/'))
        return files_list


def main():
    val = validator.Validator()
    get_files = GetFiles()
    # put your directory
    directory = ""
    # set the environment variable
    os.environ['BC_SPECIAL_WORD'] = ''
    files = get_files.get_list_of_files(directory)
    print(files)
    val.scan_files(files)


if __name__ == '__main__':
    main()