#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <windows.h>
#include <string.h>
#include <math.h>

//typedef enum
//{
//    false = 0,
//    true  = 1,
//} bool;
//
//
//typedef bool (*IsUserAnAdminFunc)();


//size_t strlcpy(char *dest, const char *src, size_t n)
//{
//    size_t len = strlen(src);
//
//    if (len < n)
//        memcpy(dest, src, len + 1);
//    else {
//        memcpy(dest, src, n - 1);
//        dest[n - 1] = '\0';
//    }
//
//    return len;
//}

//double round_c(double number)
//{
//	return (number >= 0) ? (double)(int)(number + 0.5) : (double)(int)(number - 0.5);
//}

//char* concatenate(char* dest, char* src){
//	static char desti[100];
//	strcpy(desti,dest);
//	strcat(desti,src);
//	return desti;
//}
//
//int make_directory(char* name)
//    {
//	return mkdir(name);
//    }
//
//int delete_directory(char* name)
//    {
//    return rmdir(name);
//    }
//
//int build(char* name){
//	char *array[100];
//	char *dest;
//	int i=0;
//	int dump=0;
//	int Len = -1;
//	array[i] = strtok(name,"\\");
//	while(array[i]!=NULL){array[++i] = strtok(NULL,"\\");}
//	while (array[++Len] != NULL) {;}
//	for (i=0;i<Len;i++)
//	{
//		if (i!=0){
//		dest=concatenate(array[i-1],"\\");
//		dest=concatenate(dest,array[i]);
//		array[i]=dest;
//		}
//		dump=dump+make_directory(array[i]);
//	}
//	if (dump<0){dump=-1;}
//	return dump;
//}
//
//int remove_c(char* name){
//    char *array[100];
//    char arr[100][100];
//    char *dest="";
//    int i=0;
//    int dump=0;
//    int Len=-1;
//    array[i]=strtok(name,"\\");
//    while(array[i]!=NULL){array[++i]=strtok(NULL,"\\");}
//    while(array[++Len]!=NULL){;}
//
//    for (i=0;i<Len;i++){
//        if (i!=0){
//            dest=concatenate(array[i-1],"\\");
//            dest=concatenate(dest,array[i]);
//            array[i]=dest;
//        }
//        strcpy(arr[i],array[i]);
//    }
//    printf("\n");
//    for (i=Len-1;i>=0;i--){
//        dump=dump+delete_directory(arr[i]);
//    }
//    return dump;
//}



void save_txt(char* name,int *array,int row,int column)
	{
	FILE *fp1;
	int i;
	fp1 = fopen(name, "w");
	for (i = 0; i<row*column; i++)
		{
	    fprintf(fp1, "%d%s",array[i],(i%column<column-1?",":"\n"));
		}
	fclose(fp1);
	}

void save_txt_double(char* name,double *array,int row,int column)
	{
	FILE *fp1;
	int i;
	fp1 = fopen(name, "w");
	for (i = 0; i<row*column; i++)
		{
	    fprintf(fp1, "%0.5f%s",array[i],(i%column<column-1?",":"\n"));
		}
	fclose(fp1);
	}

//void save_img(char* name,int *array,int row, int column){
//	char *named;
//	FILE *f;
//	int i;
//	named=concatenate(name,".pgm");
//	f = fopen(named, "wb");
//	fprintf(f, "P5\n%i %i 255\n", column, row);
//	for (i=0; i<row*column; ++i) {
//		 fputc(array[i], f);   // 0 .. 255
//	}
//}

//void fft_shift(double* arr,int column,int row)
//	{
//	int i;
//	double tmp;
//	int r_h=row/2;
//	int c_h=column/2;
//	int m1to3=row*c_h+c_h;
//	int m2to4=row*c_h-c_h;
//	for(i=0;i<row*column;i++)
//		{
//		if (i/column <r_h && i%column<c_h)
//			{
//			tmp=arr[i+m1to3];
//			arr[i+m1to3]=arr[i];
//			arr[i]=tmp;
//			}
//		else if (i/column <r_h && i%column>=c_h)
//			{
//			tmp=arr[i+m2to4];
//			arr[i+m2to4]=arr[i];
//			arr[i]=tmp;
//			}
//		}
//	}

//int* createArray(int column, int row)
//{
//	int i;
//	int *arr=calloc(row * column, sizeof(int));
//	for (i=0;i<row*column;i++){
//			arr[i]=i/column+i%column;
//	}
//    return arr;
//}
//
//void destroyArray(int* arr)
//{
//    free(arr);
//}

//void square_array(int* arr,int column,int row,int threshold,int min,int max){
//	int i;
//	for (i=0;i<row*column;i++)
//	{
//		if (arr[i]<threshold)
//		{
//			arr[i]=min;
//		}
//		else
//		{
//			arr[i]=max;
//		}
//	}
//}
//
//void truncuate_array(int* arr,int column,int row,int threshold,int min){
//	int i;
//	for (i=0;i<row*column;i++)
//	{
//		if (arr[i]<threshold)
//		{
//			arr[i]=min;
//		}
//	}
//}
//
//void resize(int* arr,int column_old,int row_old,int column_new,int row_new,int* array){
//    int i,k;
//    for (i=0;i<row_new*column_new;i++){
//        k=(int)(((int)i/column_new)/((double)row_new/(double)row_old))*column_old+(int)((i%column_new)/((double)column_new/(double)column_old));
//        array[i]=arr[k];
//    }
//}
//
//void circle(int* arr,int column,int row,int radius,int i_m,int j_m){
//	int i,j,g;
//	for(g=0;g<row*column;g++){
//		i=g/column;
//		j=g%column;
//		if (sqrt(pow(i-i_m,2)+pow(j-j_m,2))<=radius){arr[g]=0;}
//	}
//}

//int is_admin(void){
//    HINSTANCE Shell32Dll = LoadLibrary("Shell32.dll");
//    IsUserAnAdminFunc IsUserAnAdmin;
//    IsUserAnAdmin = (IsUserAnAdminFunc)GetProcAddress(Shell32Dll, "IsUserAnAdmin");
//    return IsUserAnAdmin();
//    }

//char swap(char source,char swapping){
//	if (source==' '){return ' ';}
//
//	if (source>='a' && source<='z'){return (source+tolower(swapping)+14)%26+'a';}
//
//	if (source>='0' && source<='9'){return (source);}
//
//	return (source+swapping)%26+'A';
//}
//
//char* vigenere(char* str,char* key){
//	int len =strlen(str);
//	int KeyLen=strlen(key);
//	char* NewKey=calloc(len, sizeof(int));
//	char* message=calloc(len, sizeof(int));
//	int i,j;
//	//newkey
//    for(i = 0, j = 0; i < len; ++i, ++j){
//        if(j == KeyLen)
//            j = 0;
//        if(str[i]==' '){NewKey[i]=' ';j--;}
//        if(str[i]>='0' && str[i]<='9'){NewKey[i]=' ';j--;}
//        else{NewKey[i] = key[j];}
//    }
//    NewKey[i] = '\0';
//	for(i = 0; i < len; ++i){
//		message[i]=swap(str[i],NewKey[i]);
//	}
//	message[i]='\0';
//	return message;
//}


//main(){
//int a=is_admin();
//printf("%d\n",a);
//
//}
