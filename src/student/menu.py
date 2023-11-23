import student.student_frame_factory as sff

def go_to_workouts(frame) -> None:
    sff.StudentFrameFactory.get_frame("WorkoutsFrame", frame.window)

def go_to_profile(frame) -> None:
    sff.StudentFrameFactory.get_frame("ProfileFrame", frame.window)