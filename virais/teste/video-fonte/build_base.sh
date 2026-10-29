set -e
seg(){ # in start dur out filter
ffmpeg -loglevel error -y -ss $2 -t $3 -i $1 -vf "$5,fps=30,setsar=1,eq=brightness=-0.04:saturation=0.92,vignette=PI/5,format=yuv420p" -an -frames:v $6 -c:v libx264 -crf 17 -preset fast $4
}
V="scale=1080*1.06:1920*1.06,crop=1080:1920:'(iw-1080)/2+t*8':'(ih-1920)/2'"
seg /home/claude/mix/clips/40128.mp4 0.5 2.8 s1.mp4 "scale=1145:2036,crop=1080:1920:'32-t*10':58" 84
seg /home/claude/mix/clips/4915.mp4 4 2.6 s2.mp4 "scale=-2:2036,crop=1080:1920:'(iw-1080)/2+t*20':58" 78
seg /home/claude/mix/clips/99909.mp4 1 2.6 s3.mp4 "scale=-2:2036,crop=1080:1920:'(iw-1080)/2+250-t*20':58" 78
seg /home/claude/mix/clips/43236.mp4 1 2.8 s4.mp4 "scale=-2:2036,crop=1080:1920:'330+t*25':58" 84
seg /home/claude/mix/clips/43231.mp4 0 2.2 s5.mp4 "scale=-2:1920,crop=1080:1920" 66
seg /home/claude/mix/clips/43242.mp4 2 3.4 s6.mp4 "scale=1145:2036,crop=1080:1920:'32+t*-8':58" 102
seg /home/claude/mix/clips/271.mp4 3 3.0 s7.mp4 "scale=-2:1920,crop=1080:1920" 90
printf "file s%d.mp4\n" 1 2 3 4 5 6 7 > list.txt
ffmpeg -loglevel error -y -f concat -safe 0 -i list.txt -c copy base.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 base.mp4
