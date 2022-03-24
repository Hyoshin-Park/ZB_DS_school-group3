def solution(record):
    answer = []
    aa = {}
    result = []
    for i in record:
        answer.append(i.split())
    for j in answer:
        if j[0] == "Enter":
            aa[j[1]] = j[2]
        
        elif j[0] == "Change":
            aa[j[1]] = j[2]
    
    for n in answer:
        if n[0] == "Enter":
            result.append(f"{aa[n[1]]}님이 들어왔습니다.")
        elif n[0] == "Leave":
            result.append(f"{aa[n[1]]}님이 나갔습니다.")
    return result
        
    

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])