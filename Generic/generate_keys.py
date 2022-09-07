import random

class prime_numbers_handling:
    def prime_check(self,n:int):
        count=0
        for i in range(1,n+1):
            if n%i==0:
                count+=1
        
        if count==2:
            return True
        else:
            return False

    def generate_prime_upto_n(self,n:int):
        prime_numbers=[]
        for number in range(0,n):
            output=self.prime_check(number)
            if output==True: 
                prime_numbers.append(number)
        
        return prime_numbers

def get_p_and_q(prime_numbers:list):
    n=len(prime_numbers)
    p=0
    q=0
    while True: 
        if p!=q:
            break
        else:
            p=prime_numbers[random.randrange(0,n)]
            q=prime_numbers[random.randrange(0,n)]
    return p,q 

def common_factor_between(phi,phi_i):
    factors_1=[]
    factors_2=[]
    for i in range(1,phi+1):
        if phi%i==0:
            factors_1.append(i)
    
    for i in range(1,phi_i+1):
        if phi_i%i==0:
            factors_2.append(i)
    
    hcf=max([value for value in factors_1 if value in factors_2])
    return hcf
    

def get_public_key_1(phi,N):
    output_keys=[]
    for i in range(2,phi+1):
        f1=common_factor_between(phi,i)
        f2=common_factor_between(N,i)
        if f1==1 and f2==1:
            output_keys.append(i)
    return output_keys

def get_private_key_1(e,phi,N):
    output_keys=[]
    for i in range(1,N):
        if (e*i%phi==1):
            output_keys.append(i)
    return output_keys

def generate_keys():
    while True: 
        p_n_handle=prime_numbers_handling()
        total_prime_numbers=p_n_handle.generate_prime_upto_n(100)
        p,q=get_p_and_q(total_prime_numbers)
        N=p*q 
        if N>2500:
            break
        
    phi=(p-1)*(q-1)
    print(p,q,phi)
    e=get_public_key_1(phi,N)
    e=e[random.randrange(int(len(e)/2),len(e))]
    d=get_private_key_1(e,phi,N)
    d=d[random.randrange(int(len(d)/2),len(d))]
    return e,d,N

def encrypt_public_key(public_key,flag):
    key=int(public_key.split('!_')[-1])
    other_key='!'.join(public_key.split('!_')[0:-1])
    final_key=''
    for i in other_key:
        if flag==0:
            i=chr(ord(i)+key)
        else: 
            i=chr(ord(i)-key)
        final_key+=i
    final_key+='!_'+str(key)
    return final_key

def get_keys():
    public_keys=[]
    private_keys=[]
    for i in range(0,5):
        public_key,private_key,N=generate_keys()
        
        public_keys.append(str(public_key))
        public_keys.append(str(N))
        public_keys.append('!')
        
        private_keys.append(str(private_key))
        private_keys.append(str(N))
        private_keys.append('!')
    
    n_k=int(random.randrange(1,23))
    public_keys.append(str(n_k))
    print(public_keys,private_keys)
    public_keys='_'.join(public_keys)
    private_keys.append(str(-1*n_k))
    private_keys='_'.join(private_keys)
    public_keys=encrypt_public_key(public_keys,0)
    print(public_keys)
    print(private_keys)
    return public_keys,private_keys