from cls import HomemadeApplication
from utils import quit_action

if __name__ == "__main__":
    app = HomemadeApplication()
    app.mainloop()
    quit_action(app)