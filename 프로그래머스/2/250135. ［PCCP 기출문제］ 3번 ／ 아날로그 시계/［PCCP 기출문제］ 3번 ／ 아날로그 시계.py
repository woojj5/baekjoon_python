def solution(h1, m1, s1, h2, m2, s2):
    start = h1*3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2
    ans = 0
    
    if start == 0 or start == 3600 * 12:
        ans+=1
    while start < end:
        h1angle = start/(3600/30)%360
        m1angle = start/(300/30)%360
        s1angle = start*(6)%360
        
        
        nh1angle = (start+1)/(3600/30)%360
        nm1angle = (start+1)/(300/30)%360
        ns1angle = (start+1)*(6)%360
        
        if nh1angle == 0:
            nh1angle = 360
                
        if nm1angle == 0:
            nm1angle = 360
                
        if ns1angle == 0:
            ns1angle = 360
        
        if nh1angle == nm1angle == ns1angle:
            ans+=1
            start+=1
            continue
        
        if s1angle < m1angle and ns1angle>= nm1angle:
            ans+=1
        
        if s1angle < h1angle and ns1angle>= nh1angle:
            ans+=1
        
        start+=1
        
    return ans