import convert_to_anime_gif as gifanime
import sys

args = sys.argv[1:]


def main():
    file_path = args[0]
    try:
        gifanime.convert_to_anime_gif(file_path)
    except Exception as e:
        print(f"エラーが発生しました: {e}")


if __name__ == "__main__":
    main()
