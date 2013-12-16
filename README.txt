INSTALLATION AND EXECUTION:
1.Download the facebook sdk for python from https://github.com/pythonforfacebook/facebook-sdk .
2.Install the facebook sdk using pip install or easy_install.
3.Create an application on facebook by logging in to your facebbok account as developer and get the access token for the app. 
4.In the Select Permissions window, select the following user data and friends data permissions:
  user_about_me, 
  user_birthday, 
  user_education_history, 
  user_friends, 
  user_groups, 
  user_hometown, 
  user_interests, 
  user_likes, 
  user_location, 
  user_relationship_details, 
  user_relationships, 
  user_status, 
  user_subscription, 
  user_work_history, 
  user_religion_politics 
  friends_about_me, 
  friends_activities, 
  friends_education_history, 
  friends_birthday, 
  friends_hometown, 
  friends_interests, 
  friends_likes, 
  friends_location, 
  friends_relationships, 
  friends_religion_politics, 
  friends_status, 
  friends_work_history.
5.Go to the code directory and open the connector.py file in the core folder. Paste the newly generated access token.
6.Run the main.py file in the code directory. 
7.You can change the threshold value in the main directory to filter the results accordingly. For example, for viewing all results, set the threshold value to 0. 
