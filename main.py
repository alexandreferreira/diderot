import requests

__author__ = 'alexandreferreira'

PIVOTAL_TOKEN = '30363b96aec8ece91d67a7ba74ab4c89'
HEADER = {'X-TrackerToken': PIVOTAL_TOKEN}


def get_projects():
    req = requests.get("https://www.pivotaltracker.com/services/v5/projects", headers=HEADER)
    if req.status_code == requests.codes.ok:
        projects = req.json()
        for project in projects:
            print "------------------------------"
            print "Project Name: %s" % project.get('name')
            users = get_user_project(project.get('id'))
            print "Users:"
            for user in users:
                print "  Name: %s - Role %s - Kind: %s - initials: %s" % (user.get('person').get('name'),
                                                                          user.get('role'),
                                                                          user.get('person').get('kind'),
                                                                          user.get('person').get('initials'))
                stories = get_stories(project.get('id'), user.get('person').get('id'))
                print "    Stories:"
                for story in stories:
                    print "      Name: %s - Type: %s - Current State: %s" % (story.get('name'), story.get('story_type'),
                                                                             story.get('current_state'))

    else:
        print "Something went wrong"


def get_user_project(project_id):
    req = requests.get("https://www.pivotaltracker.com/services/v5/projects/"+str(project_id)+"/memberships", headers=HEADER)
    if req.status_code == requests.codes.ok:
        return req.json()
    else:
        print "Something went wrong"


def get_stories(project_id, user_id):
    req = requests.get("https://www.pivotaltracker.com/services/v5/projects/%s/stories?filter=owner:%s requester:%s" %
                       (project_id, user_id, user_id), headers=HEADER)
    if req.status_code == requests.codes.ok:
        return req.json()
    else:
        print "Something went wrong"


def login():
    pass


if __name__ == '__main__':
    get_projects()