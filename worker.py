from app.actions import Actions
from app.utils.slackhelper import SlackHelper


def main():
    slackhelper = SlackHelper()
    actions = Actions(slackhelper)


if __name__ == '__main__':
    main()
