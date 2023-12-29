# gifify

OSにインストールされたFFmpegをコールして、動画をGIFアニメーションにするPythonパッケージです。subprocessでシェルにアクセスしますので事前にツールのインストールが必要です。



## ツールの依存関係
- [FFmpeg](https://ffmpeg.org/)
- [gifsicle](https://www.lcdf.org/gifsicle/)


### インストール
~~~shell
brew install ffmpeg
brew install gifsicle
~~~


### バージョン

| パッケージ | バージョン |
|:-----------|:-----------|
| FFmpeg     | 6.1        |
| gifsicle   | 1.94       |

~~~shell
ffmpeg -version
gifsicle --version
~~~


## gififyの使い方

次は、GitHubからdevelopブランチの最新コミットのgififyをインストールする例です:

~~~shell
pip3 install git+https://github.com/aragig/gifify.git@develop
~~~

次は、ローカルのgififyプロジェクトを直接インストールする例です:

~~~shell
cd gifify
pip3 install -e .
~~~

参考: https://101010.fun/programming/ffmepg-animation-gif.html
