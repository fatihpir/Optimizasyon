import math
input=[[0,0,1,1],[0,1,0,1]]
output=[0,1,1,0]
weight=[[0.129952,0.570345],[-0.923123,-0.328932],[0.341232,-0.115223],[0.164732],[0.752621],[-0.993423]]
alf=0.8
lmd=0.5
def signoid(net):return 1/(1+math.exp(-net))
def net_ara(input1,weight11,weight12,input2,weight21,weight22,threshold,weight31,weight32):return (input1*weight11+input2*weight21+threshold*weight31),(input1*weight12+input2*weight22+threshold*weight32)
def net_cikti(net1,weight11,net2,weight21,threshold,weight31):return signoid(signoid(net1)*weight11+signoid(net2)*weight21+threshold*weight31)
def error(beklenen,cikti):return (beklenen-cikti)
def sm(cikti,error):return (cikti*(1-cikti)*error)
def delta_ajm(sm,cikti):return lmd*sm*cikti+alf*0.0
for i in range(0,len(input[0]),1):
    print "\nAgirliklar:",weight
    net1,net2=net_ara(input[0][i],weight[0][0],weight[0][1],input[1][i],weight[1][0],weight[1][1],1.0,weight[2][0],weight[2][1])
    cikti=net_cikti(net1,weight[3][0],net2,weight[4][0],1.0,weight[5][0])
    print "Ara Cikti-1:",signoid(net1),"Ara Cikti-2:",signoid(net2),"Cikti:",cikti,"Hata:",error(output[i],cikti),sm(cikti,error(output[i],cikti))
    S3=signoid(net1)*(1-signoid(net1))*sm(cikti,error(output[i],cikti))*weight[3][0]
    S4=signoid(net2)*(1-signoid(net2))*sm(cikti,error(output[i],cikti))*weight[4][0]
    print "SM-3:",S3,"SM-4:",S4
    delta_A11 = delta_ajm(S3,input[0][i])
    delta_A12 = delta_ajm(S3, input[0][i])
    delta_A21 = delta_ajm(S4,input[1][i])
    delta_A22 = delta_ajm(S4, input[1][i])
    delta_A31 = delta_ajm(S3, 1.0)
    delta_A32 = delta_ajm(S4, 1.0)
    delta_A41 = delta_ajm(sm(cikti,error(output[i],cikti)),signoid(net1))
    delta_A51 = delta_ajm(sm(cikti,error(output[i],cikti)),signoid(net2))
    delta_A61 = delta_ajm(sm(cikti, error(output[i], cikti)), 1.0)
    print delta_A11," ",delta_A12," ",delta_A21," ",delta_A22," ",delta_A31," ",delta_A32," ",delta_A41," ",delta_A51," ",delta_A61,"SON"
    weight[0][0] += delta_A11
    weight[0][1] += delta_A12
    weight[1][0] += delta_A21
    weight[1][1] += delta_A22
    weight[2][0] += delta_A31
    weight[2][1] += delta_A32
    weight[3][0] += delta_A41
    weight[4][0] += delta_A51
    weight[5][0] += delta_A61
    print "Yeni agirliklar:",weight
