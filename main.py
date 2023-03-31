from post import Post
import csv
import os

# file_path = 'C:/Users/user/Desktop/python/board/data.csv'
file_path = './board/data.csv'
# Post 객체를 저장할 리스트
post_list=list()


if os.path.exists(file_path):
    print("게시물 로딩중...")
    f = open(file_path, "r",encoding="utf-8")
    reader=csv.reader(f)
    for data in reader:
        #Post 인스턴스 생성
        post = Post(int(data[0]), data[1],data[2],int(data[3]))
        post_list.append(post)

else:
    f = open(file_path, "w", encoding="utf-8", newline='')
    f.close()
    

# 게시글 쓰기
def write_post():
    """게시글 쓰기 함수"""            
    print("\n\n - 게시글 쓰기 -")
    title = input("제목을 입력해 주세요\n>>>")
    content = input("본문을 입력해 주세요\n>>>")
    id = post_list[-1].get_id()+1
    post=Post(id, title, content, 0)
    post_list.append(post)
    print("# 게시글이 등록되었습니다.")

# 게시글 목록 확인하기기
def list_post():
    """게시글 목록 함수"""
    print("\n\n - 게시글 목록 -")    
    id_list=list()
    for i in post_list:
        print(f"번호 : {i.get_id()}")        
        print(f"제목 : {i.get_title()}")
        print(f"조회수 : {i.get_view_count()}\n")
        id_list.append(i.get_id())
                
    while True:
        print("\n글번호를 선택해 주세요 (메뉴로 돌아가려면 -1을 입력)")
        try:
            id = int(input(">>>"))
            if id in id_list:
                detail_post(id)
            elif id == -1:
                break
            else :
                print("없는 글 번호 입니다.")
        except ValueError:
            print("숫자를 입력해 주세요")


def detail_post(id):
    """ 게시글 상세 보기 함수"""
    print("\n\n- 게시글 상세 -")
    for post in post_list:
        if post.get_id() == id:
            # 조회수 증가
            post.add_view_count()
            print("번호 : ", post.get_id())
            print("제목 : ", post.get_title())
            print("본문 : ", post.get_content())
            print("조회수 : ", post.get_view_count())
            targetpost = post

    while True:
        print("Q) 수정: 1 삭제 2 (메뉴로 돌아가려면 -1 입력)")
        try:
            choice=int(input(">>>"))
            if choice == 1:
                update_post(targetpost)
                break
            elif choice == 2 :
                delete_post(targetpost)
                break
            elif choice == -1 :
                break
            else : 
                print("잘못 입력하였습니다.")
        except ValueError:
            print("숫자를 입력해 주세요")

# 게시글 수정
def update_post(targetpost):
    """게시글 수정 함수"""
    print("\n\n- 게시글 수정 -")
    print("제목을 입력해 주세요")
    title = input(">>>")
    print("본문을 입력해 주세요")
    content = input(">>>")
    targetpost.set_post(targetpost.get_id(), title, content, targetpost.get_view_count())
    print("# 게시글이 수정되었습니다.")

def delete_post(targetpost):
    """게시글 삭제 함수"""
    post_list.remove(targetpost)
    print("# 게시글이 삭제되었습니다.")


def save():
    f = open(file_path, "w",encoding="utf-8", newline="")
    writer= csv.writer(f)
    for post in post_list:
        row = [post.get_id(), post.get_title(), post.get_content(), post.get_view_count()]
        writer.writerow(row)
    f.close()
    print("# 저장이 완료되었습니다.")
    print("# 프로그램종료")

# 메뉴 출력하기

while True:
    print("\n\n- FastCampus BLOG -")
    print("- 메뉴를 선택해주세요 -")
    print("1. 게시글 쓰기")
    print("2. 게시글 목록")
    print("3. 프로그램 종료")
    try :
        choice = int(input("숫자를 입력해주세요>>>"))
    except ValueError:
        print("숫자를 입력해주세요 플리즈")
        
    
    else:
        if choice == 1:
            write_post()

        elif choice == 2:
            list_post()
        
        elif choice ==3 :
            save()
            break

    
        



    