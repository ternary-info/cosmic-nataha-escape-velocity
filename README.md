# MOP "ESCAPE VELOCITY" (SynthPop Cover)

- **Target Artifact:** `NatahaHQ-escape-out1.mp4` (38.8 sec)
- **Pipeline:** Gemini/Veo -> ffmpeg -> Python 2.7 Frame Processor -> ffmpeg
- **Timeframe:** 2026-10-07 23:27 - 2026-10-08 02:15 (2h48m)
- **Maintainer:** Alexander "Shaos" Shabarshin
- **Based on:** "SLOPCORE: ESCAPE VELOCITY" by anabology
  - [Original Music Video](https://www.youtube.com/watch?v=C3fxudvU-UU)
  - [Source Files](https://drive.google.com/drive/folders/1aYcTHm00aY-Lk1lufsgSkXK-XJXWduMk)
  - [SynthPop Cover Short Video](https://www.youtube.com/shorts/GLumMK8LmjE)

[![ESCAPE VELOCITY SYNTH POP COVER](https://img.youtube.com/vi/GLumMK8LmjE/maxresdefault.jpg)](https://youtu.be/GLumMK8LmjE)

## 1. Prerequisites & Toolchain
- `ffmpeg`
- `Python` v2.7
- `ImageMagick` (`convert`)
- `mencoder` (optional for quick preview)

## 2. Step-by-Step Procedure
### Step 1
Split chosen video clips to a separate frames:

    ./vjpg NatahaHQ-escape-v03
    ./vjpg NatahaHQ-escape-v12
    ./vjpg NatahaHQ-escape-v13
    ./vjpg NatahaHQ-escape-v15
    ./vjpg NatahaHQ-escape-v16
    ./vjpg NatahaHQ-escape-v18
    ./vjpg NatahaHQ-escape-v19

### Step 2
Run NatahaHQ script to build a preview:

    ./NatahaHQ-escape-out1.py

### Step 3
Run final master encoding for Youtube:

    ffmpeg -framerate 29.97 -i "NatahaHQ-escape-out1/%06d.jpg" -i escape1.wav -vf "scale=1080:1920:flags=lanczos" -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k NatahaHQ-escape-out1.mp4

## Appendix. Description of source files with Google Flow prompts

### escape1.wav
38.8 seconds chorus of SynthPop cover of "Escape Velocity"

### anabologyN.png
Borrowed from anabology sources of "SLOPCORE: ESCAPE VELOCITY"

### NatahaHQ-happy-face.jpg
From earlier generation of Cosmic Nataha

### NatahaHQ-escape-1.jpg
Nano Banana from Gemini chat interface

- `anabology1.png`
- `NatahaHQ-happy-face.png`

Need to correct this AI image as it should have face of another AI person (look at 2nd image) 

### NatahaHQ-escape-2.jpg
Crop from one of the frames of NatahaHQ-escape-v03.mp4 (see below)

### NatahaHQ-escape-v01.mp4
Veo 3.1 - Fast (Ingredients) 9:16 8s

- `anabology1.png`
- `NatahaHQ-happy-face.png`
- `anabology0.png`

The white robotaxi from 3rd image has stopped at the head of the wet concrete catwalk inside the dark data hall with its rear door open; the woman from 1st image (make sure she is having face, haircut and earrings as showed on image 2) steps out of the car and stands upright on the catwalk facing the camera, moving in time with 132 BPM singing "Eighteen months to escape the underclass". Slow push in. No cuts.

### NatahaHQ-escape-v02.mp4
Veo 3.1 - Fast (Ingredients) 9:16 8s

- `anabology1.png`
- `anabology0.png`
- `NatahaHQ-escape-1.jpg`

The white robotaxi from 2nd image has stopped at the head of the wet concrete catwalk inside the dark data hall with its rear door open; the woman from 1st image (make sure she is having face, haircut and wearable microphone as showed on image 3) steps out of the opened side door of that robotaxi and stands upright on the catwalk facing the camera, moving in time with 132 BPM singing "Eighteen months to escape the underclass". Slow push in. No cuts.

### NatahaHQ-escape-v03.mp4
Veo 3.1 - Fast (Ingredients) 9:16 8s

- `anabology1.png`
- `anabology0.png`
- `NatahaHQ-escape-1.jpg`

The white robotaxi from 2nd image has stopped on a wet concrete floor inside the dark data hall with its side door open; the woman from 1st image (make sure she is having face, haircut and wearable microphone as showed on image 3) steps out of the opened side door of that robotaxi and stands upright facing the camera, moving in time with 132 BPM EDM moving straight to the camera direction and speaks "You have eighteen months to escape the permanent underclass. Lock in." Slow push in. No cuts. This is a music video, so everything should be photo-realistic and cinematic.

### NatahaHQ-escape-v04-bad.mp4
Veo 3.1 - Fast (Ingredients) 9:16 8s (BAD)

- `anabology1.png`
- `NatahaHQ-escape-1.jpg`

The scene from 1st image, moving in time with 132 BPM. Full-length shot: the woman from 1st image (make sure she is having face, haircut and wearable microphone as showed on image 2) walks straight toward the camera down the wet concrete catwalk with her whole body from head to boots in frame in the beginning, but then she close up and slowly says "Lock In";  fog. The camera stays wide and slowly pulls back to keep her whole figure in frame. No cuts. This is a music video, so everything should be photo-realistic and cinematic.

### NatahaHQ-escape-v05-bad.mp4
Veo 3.1 - Fast (Ingredients) 9:16 8s (BAD)

- `anabology1.png`
- `NatahaHQ-escape-1.jpg`

Full-length shot: the woman from 1st image (make sure she is having face, haircut and wearable microphone as showed on image 2) walks straight toward the camera down the wet concrete catwalk with her whole body from head to boots in frame in the beginning, but then she close up and slowly says "Lock In";  fog. The camera stays wide and slowly pulls back to keep her whole figure in frame. No cuts. This is a music video, so everything should be photo-realistic and cinematic.

### NatahaHQ-escape-v06-bad.mp4
Veo 3.1 - Fast (Ingredients) 9:16 8s (BAD)

- `anabology1.png`
- `NatahaHQ-escape-1.jpg`

Full-length shot: the woman from 1st image, but with face, haircut and wearable microphone as showed on image 2, walks straight toward the camera down the wet concrete catwalk with her whole body from head to boots in frame in the beginning, but then she close up and slowly says "Lock In";  fog. The camera stays wide and slowly pulls back to keep her whole figure in frame. No cuts. This is a music video, so everything should be photo-realistic and cinematic.

### NatahaHQ-escape-v07-bad.mp4
Veo 3.1 - Fast (Ingredients) 9:16 8s (BAD)

- `anabology1.png`
- `NatahaHQ-escape-1.jpg`

Full-length shot: the woman from 2nd image walks straight toward the camera down the wet concrete catwalk in outfit as shown on 1st image with her whole body from head to boots in frame in the beginning, but then she close up and slowly says "Lock In";  fog. The camera stays wide and slowly pulls back to keep her whole figure in frame. No cuts. This is a music video, so everything should be photo-realistic and cinematic.

### NatahaHQ-escape-v08-bad.mp4
Veo 3.1 - Fast (Ingredients) 9:16 8s (BAD)

- `anabology1.png`
- `NatahaHQ-escape-1.jpg`

Full-length shot: the woman from 2nd image (short haircut, blonde, face freckles, blue eyes, wearable mic) walks straight toward the camera down the wet concrete catwalk in outfit as shown on 1st image with her whole body from head to boots in frame in the beginning, but then she close up and slowly says "Lock In";  fog. The camera stays wide and slowly pulls back to keep her whole figure in frame. No cuts. This is a music video, so everything should be photo-realistic and cinematic.

### NatahaHQ-escape-v09.mp4
Veo 3.1 - Fast (Ingredients) 9:16 8s

- `anabology1.png`
- `NatahaHQ-escape-1.jpg`

Full-length shot: the woman from 2nd image (very short haircut, blonde, face freckles, blue eyes, wearable mic) walks straight toward the camera down the wet concrete catwalk in outfit as shown on 1st image with her whole body from head to boots in frame in the beginning, but then she close up and slowly says "Lock In";  fog. The camera stays wide and slowly pulls back to keep her whole figure in frame. No cuts. This is a music video, so everything should be photo-realistic and cinematic.

### NatahaHQ-escape-v10.mp4
Veo 3.1 - Fast (Ingredients) 9:16 8s

- `NatahaHQ-escape-1.jpg`
- `NatahaHQ-escape-2.jpg`

Full-length shot: the woman from 1st image (very short haircut, blonde, face freckles, blue eyes, wearable mic) walks straight toward the camera down the wet concrete catwalk in outfit as shown on 2nd image with her whole body from head to boots in frame in the beginning, but then she close up and slowly says "Lock In" and look into camera;  fog. The camera stays wide and slowly pulls back to keep her whole figure in frame. No cuts. This is a music video, so everything should be photo-realistic and cinematic.

### NatahaHQ-escape-v11.mp4
Veo 3.1 - Fast (Ingredients) 9:16 8s

- `NatahaHQ-escape-1.jpg`
- `NatahaHQ-escape-2.jpg`

Full-length shot: the woman from 1st image (very short haircut, blonde, face freckles, blue eyes, wearable mic) walks straight toward the camera down the wet concrete catwalk in outfit as shown on 2nd image with her whole body from head to boots in frame in the beginning, but then she close up to the camera and slowly says "Lock In" looking into camera;  fog. The camera stays wide and slowly pulls back to keep her whole figure in frame. No cuts. This is a music video, so everything should be photo-realistic and cinematic.

### NatahaHQ-escape-v12.mp4
Veo 3.1 - Fast (Ingredients) 9:16 8s

- `NatahaHQ-escape-1.jpg`

She move closely to camera and slowly says "Lock in" and then sings "Eighteen month to escape the underclass"

### NatahaHQ-escape-v13.mp4
Veo 3.1 - Fast (Ingredients) 9:16 8s

- `NatahaHQ-escape-1.jpg`
- `NatahaHQ-escape-2.jpg`

Full-length shot: the woman from 1st image (very short haircut, blonde, face freckles, blue eyes, wearable mic) walks straight toward the camera down the wet concrete catwalk in outfit as shown on 2nd image with her whole body from head to boots in frame and confidently and loudly sings "Eighteen months to escape the underclass. Lock in, baby, foot down on the gas" while looking into camera;  fog. The camera stays wide and slowly pulls back to keep her whole figure in frame. No cuts. This is a music video, so everything should be photo-realistic and cinematic.

### NatahaHQ-escape-v14.mp4
Veo 3.1 - Fast (Ingredients) 9:16 8s

- `NatahaHQ-escape-1.jpg`

She walks closely to camera and confidently and loudly sings "Feel the A.G.I. feel it coming fast. Escape velocity..."

### NatahaHQ-escape-v15.mp4
Veo 3.1 - Fast (Ingredients) 9:16 8s

- `NatahaHQ-escape-1.jpg`

She walks closely to camera and confidently and loudly sings "Feel the A.G.I. feel it coming fast. Escape velocity...". without hand jesters. Fog. NO text overlays over the screen!

### NatahaHQ-escape-v16.mp4
Veo 3.1 - Fast (Ingredients) 9:16 8s

- `NatahaHQ-escape-1.jpg`
- `NatahaHQ-escape-2.jpg`

Full-length shot: the woman from 1st image (very short haircut, blonde, face freckles, blue eyes, wearable mic) walks straight toward the camera down the wet concrete catwalk in outfit as shown on 2nd image with her whole body from head to boots in frame and calmly says "It's so over" and than loudly screams "WE'RE SO BACK!" while looking into camera;  fog. The camera stays wide and slowly pulls back to keep her whole figure in frame. No cuts. This is a music video, so everything should be photo-realistic and cinematic.

### NatahaHQ-escape-v17.mp4
Veo 3.1 - Fast (Ingredients) 9:16 8s

- `NatahaHQ-escape-1.jpg`
- `NatahaHQ-escape-2.jpg`

Full-length shot: the woman from 1st image (very short haircut, blonde, face freckles, blue eyes, wearable mic) walks straight toward the camera down the wet concrete catwalk in outfit as shown on 2nd image with her whole body from head to boots in frame and calmly asks with a smile "It's so over?" and then loudly screams "WE'RE SO BACK!" while looking into camera and then calmly again "we're so back";  fog. The camera stays wide and slowly pulls back to keep her whole figure in frame. No cuts. This is a music video, so everything should be photo-realistic and cinematic.

### NatahaHQ-escape-v18.mp4
Veo 3.1 - Fast (Ingredients) 9:16 8s

- `NatahaHQ-escape-1.jpg`

She walks closely to camera and confidently and loudly sings "We're so back!".  Fog. NO text overlays over the screen!

### NatahaHQ-escape-v19.mp4
Veo 3.1 - Fast (Ingredients) 9:16 8s

- `NatahaHQ-escape-1.jpg`

She walks closely to camera and confidently calmly says "It's all over" and a little later almost whispering "We're so back".  Fog. NO text overlays over the screen!
