import random

europe = ['Portugal', 'Serbia', 'Spain', 'Sweden', 'Italy', 'France', 'Germany', 'Belgium', 'Denmark', 'Netherlands',
          'Croatia', 'England', 'Russia']
asia = ['India', 'Japan', 'Australia', 'SouthKorea', 'Qatar', 'UAE', 'Bahrain', 'SaudiArabia']
africa = ['Algeria', 'Tunisia', 'Nigeria', 'IvoryCoast', 'Egypt', 'Ghana', 'Kenya', 'Mauritius']
south_america = ['Argentina', 'Brazil', 'Chile', 'PeurtoRico', 'Urugauy', 'Colombia', 'Peru', 'Bolivia']
# creation of the groups
europe1 = random.sample(europe, k=8)
asia1 = random.sample(asia, k=8)
africa1 = random.sample(africa, k=8)
south_america1 = random.sample(south_america, k=8)

GroupA = [europe1[0], asia1[0], africa1[0], south_america1[0]]
GroupB = [europe1[1], asia1[1], africa1[1], south_america1[1]]
GroupC = [europe1[2], asia1[2], africa1[2], south_america1[2]]
GroupD = [europe1[3], asia1[3], africa1[3], south_america1[3]]
GroupE = [europe1[4], asia1[4], africa1[4], south_america1[4]]
GroupF = [europe1[5], asia1[5], africa1[5], south_america1[5]]
GroupG = [europe1[6], asia1[6], africa1[6], south_america1[6]]
GroupH = [europe1[7], asia1[7], africa1[7], south_america1[7]]

print("                   THE GROUPS                     ")
print("GROUP A")
for i in [0, 1, 2, 3]:
    print(GroupA[i])
print("")
print("GROUP B")
for i in [0, 1, 2, 3]:
    print(GroupB[i])
print("")
print("GROUP C")
for i in [0, 1, 2, 3]:
    print(GroupC[i])
print("")
print("GROUP D")
for i in [0, 1, 2, 3]:
    print(GroupD[i])
print("")
print("GROUP E")
for i in [0, 1, 2, 3]:
    print(GroupE[i])
print("")
print("GROUP F")
for i in [0, 1, 2, 3]:
    print(GroupF[i])
print("")
print("GROUP G")
for i in [0, 1, 2, 3]:
    print(GroupG[i])
print("")
print("GROUP H")
for i in [0, 1, 2, 3]:
    print(GroupH[i])
print("")

print("                   THE PLAYOFFS                     ")


def score_table(x):
    global pt1
    global pt2
    global pt3
    global pt4
    pt1, pt2, pt3, pt4 = 0, 0, 0, 0
    a, b, c, d, e, f, g, h, o, p, k, l = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    a += random.randint(0, 6)
    b += random.randint(0, 6)
    c += random.randint(0, 6)
    d += random.randint(0, 6)
    e += random.randint(0, 6)
    f += random.randint(0, 6)
    g += random.randint(0, 6)
    h += random.randint(0, 6)
    o += random.randint(0, 6)
    p += random.randint(0, 6)
    k += random.randint(0, 6)
    l += random.randint(0, 6)

    if a >= b:
        if a == b:
            pt1 += 1
            pt2 += 1
        else:
            pt1 += 3
    else:
        pt2 += 3
    if c >= d:
        if c == d:
            pt3 += 1
            pt4 += 1
        else:
            pt3 += 3
    else:
        pt4 += 3
    if e >= f:
        if e == f:
            pt1 += 1
            pt3 += 1
        else:
            pt1 += 3
    else:
        pt3 += 3

    if g >= h:
        if g == h:
            pt2 += 1
            pt4 += 1
        else:
            pt2 += 3
    else:
        pt4 += 3
    if o >= p:
        if o == p:
            pt1 += 1
            pt4 += 1
        else:
            pt1 += 3
    else:
        pt4 += 3
    if k >= l:
        if k == l:
            pt3 += 1
            pt2 += 1
        else:
            pt3 += 3
    else:
        pt2 += 3

    pnts = [pt1, pt2, pt3, pt4]

    if (pnts[3] != pnts[2]) and (pnts[1] != pnts[0]) and (pnts[3] != pnts[1]) and (pnts[2] != pnts[0]) and (
            pnts[3] != pnts[0]) and (pnts[2] != pnts[1]):
        print(x[0] + " - {}".format(a) + "   " + x[1] + " - {}".format(b))  # 1 and 2
        print(x[2] + " - {}".format(c) + "   " + x[3] + " - {}".format(d))  # 3 and 4
        print(x[0] + " - {}".format(e) + "   " + x[2] + " - {}".format(f))  # 1 and 3
        print(x[1] + " - {}".format(g) + "   " + x[3] + " - {}".format(h))  # 2 and 4
        print(x[0] + " - {}".format(o) + "   " + x[3] + " - {}".format(p))  # 1 and 4
        print(x[2] + " - {}".format(k) + "   " + x[1] + " - {}".format(l))  # 3 and 2
        print("\nTHE QUALIFIED TEAMS")
        teams = {pt1: x[0], pt2: x[1], pt3: x[2], pt4: x[3]}
        team1 = teams[max(pnts)]
        global teama
        global teamb
        teama = team1
        pnts.remove(max(pnts))
        team2 = teams[max(pnts)]
        teamb = team2
        print(teama)
        print(teamb)
        print("\n")
    else:

        score_table(x)


global team1, team2, team3, team4, team5, team6, team7, team8, team9, team10, team11, team12, team13, team14, team15, team16
print("GROUP A")
score_table(GroupA)
team1 = teama
team2 = teamb
print("GROUP B")
score_table(GroupB)
team3 = teama
team4 = teamb
print("GROUP C")
score_table(GroupC)
team5 = teama
team6 = teamb
print("GROUP D")
score_table(GroupD)
team7 = teama
team8 = teamb
print("GROUP E")
score_table(GroupE)
team9 = teama
team10 = teamb
print("GROUP F")
score_table(GroupF)
team11 = teama
team12 = teamb
print("GROUP G")
score_table(GroupG)
team13 = teama
team14 = teamb
print("GROUP H")
score_table(GroupH)
team15 = teama
team16 = teamb
print("\n")
print("                   THE LAST SIXTEEN                     ")
print("\n")


def last_sixteen(team1, team2, team3, team4, team5, team6, team7, team8, team9, team10, team11, team12, team13, team14,
                 team15, team16):
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    a += random.randint(0, 6)
    b += random.randint(0, 6)
    c += random.randint(0, 6)
    d += random.randint(0, 6)
    e += random.randint(0, 6)
    f += random.randint(0, 6)
    g += random.randint(0, 6)
    h += random.randint(0, 6)
    i += random.randint(0, 6)
    j += random.randint(0, 6)
    k += random.randint(0, 6)
    l += random.randint(0, 6)
    m += random.randint(0, 6)
    n += random.randint(0, 6)
    o += random.randint(0, 6)
    p += random.randint(0, 6)

    if a != b and c != d and e != f and g != h and i != j and k != l and m != n and o != p:
        print(team1 + " - {}".format(a) + "   " + team4 + " - {}".format(b))
        print(team2 + " - {}".format(c) + "   " + team3 + " - {}".format(d))
        print(team5 + " - {}".format(e) + "   " + team8 + " - {}".format(f))
        print(team6 + " - {}".format(g) + "   " + team7 + " - {}".format(h))
        print(team9 + " - {}".format(i) + "   " + team12 + " - {}".format(j))
        print(team10 + " - {}".format(k) + "   " + team11 + " - {}".format(l))
        print(team13 + " - {}".format(m) + "   " + team16 + " - {}".format(n))
        print(team14 + " - {}".format(o) + "   " + team15 + " - {}".format(p))
        global q1, q2, q3, q4, q5, q6, q7, q8
        if a > b:
            q1 = team1
        elif b > a:
            q1 = team4
        if c > d:
            q2 = team2
        elif d > c:
            q2 = team3
        if e > f:
            q3 = team5
        elif f > e:
            q3 = team8
        if g > h:
            q4 = team6
        elif h > g:
            q4 = team7
        if i > j:
            q5 = team9
        elif j > i:
            q5 = team12
        if k > l:
            q6 = team10
        elif l > k:
            q6 = team11
        if m > n:
            q7 = team13
        elif n > m:
            q7 = team16
        if o > p:
            q8 = team14
        elif p > o:
            q8 = team15

    else:
        last_sixteen(team1, team2, team3, team4, team5, team6, team7, team8, team9, team10, team11, team12, team13,
                     team14, team15, team16)


last_sixteen(team1, team2, team3, team4, team5, team6, team7, team8, team9, team10, team11, team12, team13, team14,
             team15, team16)
print("\n")
print("THE QUALIFIED TEAMS")
print(q1, q2, q3, q4, q5, q6, q7, q8)
print("\n")
print("                   THE QUARTER FINALS                    ")


def quarters(q1, q2, q3, q4, q5, q6, q7, q8):
    a, b, c, d, e, f, g, h = 0, 0, 0, 0, 0, 0, 0, 0
    a += random.randint(0, 6)
    b += random.randint(0, 6)
    c += random.randint(0, 6)
    d += random.randint(0, 6)
    e += random.randint(0, 6)
    f += random.randint(0, 6)
    g += random.randint(0, 6)
    h += random.randint(0, 6)
    if a != b and c != d and e != f and g != h:
        print(q1 + " - {}".format(a) + "   " + q3 + " - {}".format(b))
        print(q2 + " - {}".format(c) + "   " + q4 + " - {}".format(d))
        print(q5 + " - {}".format(e) + "   " + q7 + " - {}".format(f))
        print(q6 + " - {}".format(g) + "   " + q8 + " - {}".format(h))
        global s1, s2, s3, s4
        if a > b:
            s1 = q1
        elif b > a:
            s1 = q3
        if c > d:
            s2 = q2
        elif d > c:
            s2 = q4
        if e > f:
            s3 = q5
        elif f > e:
            s3 = q7
        if g > h:
            s4 = q6
        elif h > g:
            s4 = q8

    else:
        quarters(q1, q2, q3, q4, q5, q6, q7, q8)


quarters(q1, q2, q3, q4, q5, q6, q7, q8)
print("\n")
print("THE QUALIFIED TEAMS")
print(s1, s2, s3, s4)
print("\n")
print("                   THE SEMI-FINALS                    ")


def semis(s1, s2, s3, s4):
    a, b, c, d = 0, 0, 0, 0
    a += random.randint(0, 6)
    b += random.randint(0, 6)
    c += random.randint(0, 6)
    d += random.randint(0, 6)
    if a != b and c != d:
        print(s1 + " - {}".format(a) + "   " + s2 + " - {}".format(b))
        print(s3 + " - {}".format(c) + "   " + s4 + " - {}".format(d))
        global f1, f2
        if a > b:
            f1 = s1
        elif b > a:
            f1 = s2
        if c > d:
            f2 = s3
        elif d > c:
            f2 = s4
        print("\n")
    else:
        semis(s1, s2, s3, s4)

    print(f1 + " VS " + f2)
    print("\n")


semis(s1, s2, s3, s4)


def final(f1, f2):
    a, b = 0, 0
    a += random.randint(0, 6)
    b += random.randint(0, 6)
    if a != b:
        print(f1 + " - {}".format(a) + "   " + f2 + " - {}".format(b))
        print("\n")
        if a > b:
            print(f1 + " WINS THE WORLD CUP!")
        elif b > a:
            print(f2 + " WINS THE WORLD CUP!")
    else:
        final(f1, f2)


final(f1, f2)