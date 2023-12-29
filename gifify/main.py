import subprocess
import os


def convert_to_anime_gif(input_file, scale=360):
    output_file = f"{os.path.splitext(input_file)[0]}_anime.gif"
    tmp_file = f"tmp_{os.path.splitext(input_file)[0]}_anime.gif"

    # ffmpegコマンドを実行してパレットを生成
    subprocess.run([
        "ffmpeg", "-i", input_file,
        "-vf", f"fps=15,scale={scale}:-1:flags=lanczos,palettegen=stats_mode=diff", "palette.png"
    ])
    # ffmpeg -i input_file -vf "fps=15,scale=360:-1:flags=lanczos,palettegen=stats_mode=diff" -y palette.png

    # ffmpegを使用してGIFを生成
    subprocess.run([
        "ffmpeg", "-i", input_file, "-i", "palette.png",
        "-filter_complex", f"fps=15,scale={scale}:-1:flags=lanczos[x];[x][1:v]paletteuse",
        tmp_file
    ])

    # gifsicleを使用してGIFを最適化
    subprocess.run([
        "gifsicle", "-O3", "--colors=128", "--lossy=30", tmp_file, "-o", output_file
    ])

    # 一時ファイルとパレットを削除
    os.remove("palette.png")
    os.remove(tmp_file)

    return output_file, scale
