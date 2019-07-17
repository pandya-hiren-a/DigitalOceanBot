from app.actions import Actions
from app.utils.slackhelper import SlackHelper

''' Worker should initialize the slackhelper class as well as Actions class '''


def main():
    slackhelper = SlackHelper()
    actions = Actions(slackhelper)


if __name__ == '__main__':
    main()
