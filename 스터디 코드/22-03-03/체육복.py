def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost] # 만약 잃어버려도 본인게 있으면 사용할 수 있음
    _lost = [l for l in lost if l not in reserve] # 잃어버려도 이미 한개 있어서 잃어버린게 아님
    for r in _reserve:
        f = r - 1 # 여분있는사람의 앞의 사람
        b = r + 1 # 여분있는사람의 뒷 사람
        if f in _lost: # 만약 앞사람 이 잃어버렸으면
            _lost.remove(f) # 체육복을 빌려주고 잃어버린 사람에서 제거
        elif b in _lost: # 만약 쉿사람이 잃어버렸으면
            _lost.remove(b) # 체육복을 빌려주고 잃어버린 사람에서 제거
    return n - len(_lost) # 전체에서 남은 체육복 없는 사람을 빼주기