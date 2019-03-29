AWS Farget CD Lab
===

## Demo

## What's Farget & How We Implement Severless CD

## What you will learn

* How to use git

## Installation 
The whole lab will require us to do the following installation before we get our hands dirty.

* [Create an AWS account](https://aws.amazon.com/resources/create) (if you not have one)
* [Install aws-cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
* [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## The Whole Picture

Step1. Create a repository

## Get Started 

###  Step 1 - Checkout From SCM

#### 1.1 Set up aws-cli environment
Before we start this lab, we need to [set up the aws-cli environment](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html).
In this lab, we set the region as **us-east-1**.
```
foo@bar:~$ aws configure
AWS Access Key ID [None]:
AWS Secret Access Key [None]:
Default region name [us-east-1]:
Default output format [None]:
```
After set up successfully, you can type this command to test the power of aws-cli to view the s3 bucket on your command line interface. 
```
foo@bar:~$ aws s3 ls
```


#### 1.2 Add Public Key To IAM
For the security reason, add the public key to IAM User
```
foo@bar:~$ cd ~/.ssh
foo@bar:~/.ssh$ ssh-keygen
foo@bar:~/.ssh$ aws iam upload-ssh-public-key --user-name [IAM-USER-NAME] --ssh-public-key-body "$(< ~/.ssh/id_rsa.pub)"
```
Note that this SSH public key can only be used  for authenticating the associated IAM user to an AWS CodeCommit repository.

Please refer the following links if you encounter any issue:
* [how to gen ssh public key](https://git-scm.com/book/zh-tw/v1/%E4%BC%BA%E6%9C%8D%E5%99%A8%E4%B8%8A%E7%9A%84-Git-%E7%94%9F%E6%88%90-SSH-%E5%85%AC%E9%96%8B%E9%87%91%E9%91%B0)
* [aws-cli iam document](https://docs.aws.amazon.com/cli/latest/reference/iam/upload-ssh-public-key.html)

#### 1.2 Create A Repository

Now we can create a new repository in codecommit
```
foo@bar:~/.ssh$ aws codecommit create-repository --repository-name fargate-welcomer
```
After running the create-repository command, the CLI spits back a clone url, which we will use later.

#### 1.3 Set up the .ssh/config & clone the repository

Rememer that in Step 1.2, we bind the SSH public to the IAM user, now we would like to clone the repository.
To clone the repository with ssh key, we have to enable the ssh config.

```
foo@bar:~$ vim ~/.ssh/config
```
set ~/.ssh/config as the following, and note that you can find your IAM SSH Key in your AWS account-> IAM -> Users.
```
Host git-codecommit.us-east-1.amazonaws.com
  User <IAM-SSH-KEY>
  IdentityFile ~/.ssh/id_rsa
```

now you can clone the repository with the url link. 
```
foo@bar:~/Desktop$ git clone ssh://git-codecommit.us-east-1.amazonaws.com/v1/repos/fargate-welcomer
```

#### 1.4 Set up the remote git repository
Here is the simple python program to print helloworld with Flask framework. 

In this step we will set the remote git repository, to get the code from external repository into our codecommit repository.

I will add my own repository on my github as remote, of course you can use mine or copy the code into your repo.
```
foo@bar:~/Desktop/fargate-welcomer$ git remote add github github.com:RickyWooo/AWS_Farget_CICD_Lab.git
```

* [Git remote guide](https://git-scm.com/book/zh-tw/v1/Git-%E5%9F%BA%E7%A4%8E-%E8%88%87%E9%81%A0%E7%AB%AF%E5%8D%94%E5%90%8C%E5%B7%A5%E4%BD%9C)

Change the remote URL from SSH to HTML (I prefer this way)
```
foo@bar:~/Desktop/fargate-welcomer$ git remote set-url github https://github.com/RickyWooo/AWS_Farget_CICD_Lab.git

foo@bar:~/Desktop/fargate-welcomer$ git pull github master
```
