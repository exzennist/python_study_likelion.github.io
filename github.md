## github 올리기 

**1. 레퍼지토리 생성 (이름.github.io )**

**2.  git config --global user.email"이메일"**
**3.  git config --user.name"이름"**
    * 사용자 정보 설정 (컴퓨터당 최초 1회)

**4. git init**
   * Initalied...가 뜨면 성공

**4. git add .**
    * 모든 파일을 Staging Area로 이동 

**5.  git.status 로 상태 확인 

**6. git commit -m "first commit"**
**7. git remote add origin 깃허브 주소**
    * 깃허브 주소 : http://github.com/아이디/레포명

**8. git push --set-upstream origin 브랜치명**
    * 브랜치명 : 파란괄호(master, main)

**9. 코드 수정 후 반복**
* git add . 
* git commit -m "second commit"
* git push