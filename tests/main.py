import sys
import gifify

args = sys.argv[1:]


def main():
    file_path = args[0]
    try:
        gifify.convert_to_anime_gif(file_path)
        # gifanime.convert_to_anime_gif(file_path)
    except Exception as e:
        print(f"エラーが発生しました: {e}")


if __name__ == "__main__":
    main()
