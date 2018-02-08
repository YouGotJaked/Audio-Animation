import c4d

def on_beat(frame,bpm,fps):
    return frame % beats_per_frame(bpm,fps) == 0

# hertz
def beats_per_sec(bpm):
    return bpm / 60.0

# frequency
def sec_per_beat(bpm):
    return 1 / beats_per_sec(bpm)

def beats_per_frame(bpm,fps):
    return sec_per_beat(bpm) * fps

def even(frame):
    return frame % 2 == 0

# returns standard list of frames to keyframe
def keyframes(lo,hi,bpm,fps):
    lst = []
    for i in xrange(lo,hi):
        if on_beat(i,bpm,fps):
            lst.append(i)
    return lst

# returns extended list of frames to keyframe
def keyframes_ext(lo,hi,bpm,fps,dur):
    lst = []
    for i in xrange(lo,hi):
        if on_beat(i,bpm,fps):
            lst.extend(range(i,i+dur))
    print lst
    return lst

# set keyframe
def set_keyframe(frame,hi,lo,bpm,fps):
    if frame in keyframes(hi,lo,bpm,fps):
        return 0 #do something

def main():
    doc.SetFps(60)
    fps = doc.GetFps()
    doc_time = doc.GetTime()
    curr_frame = doc_time.GetFrame(fps)
    min_frame = doc.GetMinTime().GetFrame(fps)
    max_frame = doc.GetMaxTime().GetFrame(fps)
    obj = c4d.BaseObject(c4d.Ocube)
    
    if curr_frame in keyframes_ext(min_frame,max_frame,75,fps,5):
        scale = 1.5
        h_rot = 0 #h=y
        p_rot = 0 #p=x 1.575 is full
        b_rot = 0 #b=z 0.7875 is half
    else:
        scale = 1
        h_rot = 0
        p_rot = 0
        b_rot = 0
    
    obj.SetRelScale(c4d.Vector(scale,scale,scale))
    obj.SetRelRot(c4d.Vector(p_rot,h_rot,b_rot))
    return obj

if __name__ == '__main__':
    main()
    c4d.EventAdd()
