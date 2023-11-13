# Conversion from WEBM to MOV.

On my personal experience I have not found a normal application for converting WEBM to MOV in HDR and I decided to write
my own code for this conversion.

### For use this program you need install ffmpeg

If you encounter the error '/bin/sh: ffmpeg: command not found,' it means that FFmpeg is not installed, or its path is
not in the PATH environment variable.

To install FFmpeg, you can use the package manager of your operating system. Here's how you can do it for some popular
systems:

**For Ubuntu/Debian:**

```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

**For CentOS:**

```bash
sudo yum install epel-release
sudo yum install ffmpeg
```

**For macOS:**

```bash
brew install ffmpeg
```

If you are using Windows, you can download the FFmpeg binary from
the [official FFmpeg website](https://ffmpeg.org/download.html) and add its path to the PATH environment variable.

After installing FFmpeg, make sure that the `ffmpeg` command is available from your terminal or Python command line. If
you need to specify the full path to ffmpeg in your Python code, replace `'ffmpeg'` with the full path to the
executable, for example, `'/usr/bin/ffmpeg'` for Linux.

After installing FFmpeg, try running your Python script again.

