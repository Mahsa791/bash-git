
##from github import Github
##from  git import Repo
##
##token = '2228821990bc5e74ef67aaa6e44c970cb5c9cbf2 '
##g = Github(token)
##
##repo_dir = 'Doc'
##repo = Repo(repo_dir)
##file_list = ['/Doc/test.csv']
##commit_message = 'Add TEST_2'
##repo.index.add(file_list)
##repo.index.commit(commit_message)
##remote = repo.create_remote('test.csv', url='https://github.com/Mahsa791/Test-git.git')
####origin = repo.remote('origin')

##remote.push()




##from github import Github
##import git
##
##g = Github("22c34f753fc0e78c051ada0c622e8d0ef2adb56d")
##for repo in g.get_user().get_repos():
##    print(repo.name)
##
##repo = git.Repo.init('/home/pi/Desktop')
##
##file = ['home/pi/Desktop/Test-git/test_1.csv'] #path to file to push
##file2 =['home/pi/Desktop/Test-git/README.md']
##repo.git.add([file,file2]) # same as git add file
##repo.git.commit(m = "commit message") # same as git commit -m "commit message"
##repo.git.push('Test-git', 'HEAD:master') # git push remote_to_push HEAD:m


##from github import Github
##from  git import Repo
##import git
##g = Github("22c34f753fc0e78c051ada0c622e8d0ef2adb56d")
##repo = git.Repo.init('/home/pi/Desktop/Test-git')
##code=g.get_repo('Test-git')
##file_list = ['/home/pi/Desktop/Test-git/branch1.csv']
##repo.git.add(file_list)
##
##repo = Repo(repo_dir)
####file_list = ['/Doc/test.csv']
##commit_message = 'Add TEST_2'
##repo.index.add(file_list)
##repo.index.commit(commit_message)
##remote = repo.create_remote('test.csv', url='https://github.com/Mahsa791/Test-git.git')
##remote.push()

##from github import Github
##from  git import Repo
##import git
##
##g = Github("22c34f753fc0e78c051ada0c622e8d0ef2adb56d")
##for repo in g.get_user().get_repos():
## print(repo.name)
## 
##repo = git.Repo.init('/home/pi/Desktop')
##code=g.get_repo('git_test')
##
##file ='/home/pi/Desktop/git_test/README.md'
##repo.git.add(file)
##repo.git.commit(m = "commit message")
####remote = repo.create_remote('test.csv', url='https://github.com/Mahsa791/git_test-1.git')
####origin = repo.remote('origin')
##repo.git.push('git_test', 'HEAD:master')



from github import Github
from  git import Repo
import git
g = Github("22c34f753fc0e78c051ada0c622e8d0ef2adb56d")

for repo in g.get_user().get_repos():
 print(repo.name)

repo = git.Repo.init('/home/pi/Desktop')
code=g.get_repo('git_test-1')
file ='/home/pi/Desktop/git_test-1/test-1.csv'
repo.git.add(file)
repo.git.commit(m = "commit message")
##origin = repo.remote('origin')
repo.git.push('git_test-1', 'HEAD:master')

                            
