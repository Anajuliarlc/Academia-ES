import student.student_frame_factory as sff

def request_change(frame) -> None:
        sff.StudentFrameFactory.get_frame("RequestChangeFrame", frame.window)
        frame.destroy()

def go_to_increase(frame) -> None:
            sff.StudentFrameFactory.get_frame("IncreaseFrame", frame.window)
            frame.destroy()