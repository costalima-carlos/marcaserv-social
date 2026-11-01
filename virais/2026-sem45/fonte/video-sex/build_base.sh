set -e
# Sexta 06/11 — "Um barbeiro doente. 6 clientes." Cortes por nº de frames (30 fps): 84,78,78,78,66,90,90 = 564 (18,8 s)
M=/home/claude/mix/clips
seg(){ # in start dur out filter frames
ffmpeg -loglevel error -y -ss $2 -t $3 -i $1 -vf "$5,fps=30,setsar=1,eq=brightness=-0.04:saturation=0.92,vignette=PI/5,format=yuv420p" -an -frames:v $6 -c:v libx264 -crf 17 -preset fast $4
}
seg $M/363.mp4 0.5 3.0 s1.mp4 "scale=-2:2036,crop=1080:1920:'(iw-1080)/2-60+t*20':58" 84
seg $M/144.mp4 3.0 2.8 s2.mp4 "scale=-2:2036,crop=1080:1920:'(iw-1080)/2-250+t*18':58" 78
seg $M/39855.mp4 1.0 2.8 s3.mp4 "scale=1145:2036,crop=1080:1920:'32-t*10':58" 78
seg $M/28893.mp4 2.0 2.8 s4.mp4 "scale=-2:2036,crop=1080:1920:'(iw-1080)/2+t*20':58" 78
seg $M/28897.mp4 2.0 2.4 s5.mp4 "scale=-2:1920,crop=1080:1920" 66
seg $M/40127.mp4 0.5 3.2 s6.mp4 "scale=1145:2036,crop=1080:1920:'32+t*-8':58" 90
seg $M/28897.mp4 5.0 3.2 s7.mp4 "scale=-2:2036,crop=1080:1920:'(iw-1080)/2+t*15':58" 90
printf "file s%d.mp4\n" 1 2 3 4 5 6 7 > list.txt
ffmpeg -loglevel error -y -f concat -safe 0 -i list.txt -c copy base.mp4
ffprobe -v error -count_frames -show_entries stream=nb_read_frames -show_entries format=duration -of csv=p=0 base.mp4
