from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def generate_video(text, output_filename="output.mp4"):
    clip = VideoFileClip("sample_background.mp4")
    txt_clip = TextClip(text, fontsize=70, color='white')
    txt_clip = txt_clip.set_position('center').set_duration(clip.duration)
    final_clip = CompositeVideoClip([clip, txt_clip])
    final_clip.write_videofile(output_filename, codec="libx264")
