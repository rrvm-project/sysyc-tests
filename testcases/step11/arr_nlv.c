int main(){
    int a[2][3][4];
    a[1][2][3] = 5;
    a[0][0][2] = a[1][2][3];
    return a[1][2][3] + a[0][0][2];
}