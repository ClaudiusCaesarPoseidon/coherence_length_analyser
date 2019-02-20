#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include "uEye_defines.h"

typedef int (*is_GetNumberOfCamerasFunc)(int*);
typedef int (*is_InitCameraFunc)(HIDS*,HWND);
typedef int (*is_ExitCameraFunc)(HIDS);
typedef int (*is_SetGainBoostFunc)(HIDS,INT);
typedef int (*is_BlacklevelFunc)(HIDS,UINT,void*,UINT);
typedef int (*is_SetHardwareGainFunc)(HIDS,INT,INT,INT,INT);
typedef int (*is_ExposureFunc)(HIDS,UINT,void*,UINT);
typedef int (*is_SetAutoParameterFunc)(HIDS,INT,double*,double*);
typedef int (*is_CaptureVideoFunc)(HIDS,INT);
typedef int (*is_EnableAutoExitFunc)(HIDS,INT);
typedef int (*is_SetColorModeFunc)(HIDS,INT);
typedef int (*is_SetExternalTriggerFunc)(HIDS,INT);
typedef int (*is_AllocImageMemFunc)(HIDS,INT,INT,INT,char**,INT*);
typedef int (*is_SetImageMemFunc)(HIDS,char*,INT);
typedef int (*is_CopyImageMemFunc)(HIDS,char*,INT,INT);
typedef int (*is_GetFrameTimeRangeFunc)(HIDS, double*, double*, double*);
typedef int (*is_SetFrameRateFunc)(HIDS, double, double*);


typedef struct Tupe{
	int a;
	int b;
}Tupe;


typedef struct Alloc{
	char* Mem;
	int   id;
	int   glubber;
}Alloc;

typedef struct FrameRate {
    double min;
    double max;
    double intervall;
}FrameRate;

double is_SetFrameRate_Dll(HIDS cam, double FPS,char* path){
    double newFPS = 0;
    int a=444;
    HINSTANCE uEyeDll = LoadLibrary(path);
    is_SetFrameRateFunc is_SetFrameRate;
    is_SetFrameRate = (is_SetFrameRateFunc)GetProcAddress(uEyeDll, "is_SetFrameRate");
    a=is_SetFrameRate(cam,FPS,&newFPS);
    return newFPS;
}

struct FrameRate is_GetFrameTimeRange_Dll(HIDS cam, double min, double max, double intervall, char* path){
    struct FrameRate frame_rate;
    int a=444;
    HINSTANCE uEyeDll = LoadLibrary(path);
    is_GetFrameTimeRangeFunc is_GetFrameTimeRange;
    is_GetFrameTimeRange = (is_GetFrameTimeRangeFunc)GetProcAddress(uEyeDll, "is_GetFrameTimeRange");
    a=is_GetFrameTimeRange(cam,&min,&max,&intervall);
    frame_rate.min = min;
    frame_rate.max = max;
    frame_rate.intervall = intervall;
    return frame_rate;
}

int is_getNumberofCameras_Dll(char* path){
	int pnNumCams=0;
	int a=444;
	HINSTANCE uEyeDll = LoadLibrary(path);
	is_GetNumberOfCamerasFunc is_GetNumberOfCameras;
	is_GetNumberOfCameras = (is_GetNumberOfCamerasFunc)GetProcAddress(uEyeDll, "is_GetNumberOfCameras");
	a=is_GetNumberOfCameras(&pnNumCams);
	//FreeLibrary(uEyeDll);
	return pnNumCams;

}

HIDS is_InitCamera_Dll(char* path){
	HIDS cam=0;
	HWND hWnd=NULL;
	int a=444;
	HINSTANCE uEyeDll = LoadLibrary(path);
	is_InitCameraFunc is_InitCamera;
	is_InitCamera = (is_InitCameraFunc)GetProcAddress(uEyeDll, "is_InitCamera");
	a=is_InitCamera(&cam,hWnd);
	//FreeLibrary(uEyeDll);
	return cam;
}

INT is_ExitCamera_Dll(HIDS cam,char* path){
	int result=444;
	HINSTANCE uEyeDll = LoadLibrary(path);
	is_ExitCameraFunc is_ExitCamera;
	is_ExitCamera = (is_ExitCameraFunc)GetProcAddress(uEyeDll, "is_ExitCamera");
	result=is_ExitCamera(cam);
	FreeLibrary(uEyeDll);
	return result;
}

INT is_SetGainBoost_Dll(HIDS cam, INT mode,char* path){
	int result;
	HINSTANCE uEyeDll = LoadLibrary(path);
	is_SetGainBoostFunc is_SetGainBoost;
	is_SetGainBoost = (is_SetGainBoostFunc)GetProcAddress(uEyeDll, "is_SetGainBoost");
	result=is_SetGainBoost(cam,mode);
	return result;
}

INT is_Blacklevel_Dll(HIDS cam,INT command,int param,char* path){
	INT result;
	HINSTANCE uEyeDll = LoadLibrary(path);
	is_BlacklevelFunc is_Blacklevel;
	is_Blacklevel=(is_BlacklevelFunc)GetProcAddress(uEyeDll,"is_Blacklevel");
	result=is_Blacklevel(cam,command,(void*)&param,sizeof(param));
	return result;
}

INT is_SetHardwareGain_Dll(HIDS cam,INT master,INT red, INT green, INT blue,char* path){
	INT result;
	HINSTANCE uEyeDll = LoadLibrary(path);
	is_SetHardwareGainFunc is_SetHardwareGain;
	is_SetHardwareGain=(is_SetHardwareGainFunc)GetProcAddress(uEyeDll,"is_SetHardwareGain");
	result=is_SetHardwareGain(cam,master,red,green,blue);
	return result;
}

double is_Exposure_Dll(HIDS cam,INT command, double param,char* path){
	int a;
	HINSTANCE uEyeDll = LoadLibrary(path);
	is_ExposureFunc is_Exposure;
	is_Exposure=(is_ExposureFunc)GetProcAddress(uEyeDll,"is_Exposure");
	a=is_Exposure(cam,command,(void*)&param,sizeof(param));
	return param;
}

INT is_SetAutoParameter_Dll(HIDS cam,INT param,double pval1,double pval2,char* path){
	int a;
//	printf("AAAAHHHHHHHHRRRGGGGGGG:%d\n",a);
	HINSTANCE uEyeDll = LoadLibrary(path);
	is_SetAutoParameterFunc is_SetAutoParameter;
	is_SetAutoParameter=(is_SetAutoParameterFunc)GetProcAddress(uEyeDll,"is_SetAutoParameter");
	a=is_SetAutoParameter(cam,param,&pval1,&pval2);
	return a;
}

INT is_CaptureVideo_Dll(HIDS cam,INT wait,char* path){
	int a;
	HINSTANCE uEyeDll = LoadLibrary(path);
	is_CaptureVideoFunc is_CaptureVideo;
	is_CaptureVideo=(is_CaptureVideoFunc)GetProcAddress(uEyeDll,"is_CaptureVideo");
	a=is_CaptureVideo(cam,wait);
	return a;
}

INT is_EnableAutoExit_Dll(HIDS cam,INT mode,char* path){
	int a;
	HINSTANCE uEyeDll = LoadLibrary(path);
	is_EnableAutoExitFunc is_EnableAutoExit;
	is_EnableAutoExit=(is_EnableAutoExitFunc)GetProcAddress(uEyeDll,"is_EnableAutoExit");
	a=is_EnableAutoExit(cam,mode);
	return a;
}

INT is_SetColorMode_Dll(HIDS cam, INT mode,char* path){
	int a;
	HINSTANCE uEyeDll = LoadLibrary(path);
	is_SetColorModeFunc is_SetColorMode;
	is_SetColorMode=(is_SetColorModeFunc)GetProcAddress(uEyeDll,"is_SetColorMode");
	a=is_SetColorMode(cam,mode);
	return a;
}

INT is_SetExternalTrigger_Dll(HIDS cam, INT mode,char* path){
	int a;
	HINSTANCE uEyeDll = LoadLibrary(path);
	is_SetExternalTriggerFunc is_SetExternalTrigger;
	is_SetExternalTrigger=(is_SetExternalTriggerFunc)GetProcAddress(uEyeDll,"is_SetExternalTrigger");
	a=is_SetExternalTrigger(cam,mode);
	return a;
}

struct Alloc is_AllocImageMem_Dll(HIDS cam,int width,int heigth,int bitspixel,char* path){
	struct Alloc alloc;
	int pid=0,a;
	char* pcImgMem=NULL;
	//pcImgMem=NULL;
	HINSTANCE uEyeDll = LoadLibrary(path);
	is_AllocImageMemFunc is_AllocImageMem;
	is_AllocImageMem=(is_AllocImageMemFunc)GetProcAddress(uEyeDll,"is_AllocImageMem");
    a=is_AllocImageMem(cam,width,heigth,bitspixel,&pcImgMem,&pid);
	alloc.Mem=pcImgMem;
	alloc.id=pid;
	alloc.glubber=a;
	return alloc;
}

//int is_AllocImageMem_Dll(HIDS cam,int width,int heigth,int bitspixel, char* pcImgMem,int pid){
//	HINSTANCE uEyeDll = LoadLibrary("uEye_api.dll");
//	is_AllocImageMemFunc is_AllocImageMem;
//	struct Alloc alloc;
//	int a;
////	int pid=0,a;
////	char* pcImgMem=NULL;
//	pcImgMem=NULL;
//	pid=0;
//	is_AllocImageMem=(is_AllocImageMemFunc)GetProcAddress(uEyeDll,"is_AllocImageMem");
//    a=is_AllocImageMem(cam,width,heigth,bitspixel,&pcImgMem,&pid);
//	alloc.Mem=pcImgMem;
//	alloc.id=pid;
//	alloc.glubber=a;
//	return a;
//}

INT is_SetImageMem_Dll(HIDS cam,char* pcImgMem,INT pid,char* path){
	HINSTANCE uEyeDll = LoadLibrary(path);
	is_SetImageMemFunc is_SetImageMem;
	INT a;
	is_SetImageMem=(is_SetImageMemFunc)GetProcAddress(uEyeDll,"is_SetImageMem");
	a=is_SetImageMem(cam, pcImgMem, pid);
	return a;
}

INT is_CopyImageMem_Dll(HIDS cam,char* pcImgMem, INT pid,INT dest,char* path){
	int a;
	HINSTANCE uEyeDll = LoadLibrary(path);
	is_CopyImageMemFunc is_CopyImageMem;
	is_CopyImageMem=(is_CopyImageMemFunc)GetProcAddress(uEyeDll,"is_CopyImageMemFunc");
	a=is_CopyImageMem(cam,pcImgMem,pid,dest);
	return a;
}

struct Tupe rr(int i,int j){
	struct Tupe r={i,j};
	return r;
}


int main(){
//struct Alloc al;
HIDS cam=-1;
INT nRet=-1;
//int glub=-1;
//int blah=-1;
//
//cam=is_InitCamera_Dll();
//printf("%d\n",cam);
//
//nRet=is_SetExternalTrigger_Dll(cam,IS_SET_TRIGGER_SOFTWARE);
//printf("%d\n",nRet);
//
//al=is_AllocImageMem_Dll(cam,640,480,8);
//size_t len = strlen(al.Mem);
//printf("%d\n",al.id);
//printf("%d\n",len);
//glub=is_SetImageMem_Dll(cam,al.Mem,al.id);
//printf("Glubber:%d\n",glub);
//
//blah=is_SetAutoParameter_Dll(cam,IS_SET_ENABLE_AUTO_GAIN,1,0);
//printf("Blah:%d\n",blah);
//system("PAUSE");
//is_ExitCamera_Dll(cam);
//char* a="12345";
//char* b="1234h";
//int ab=isdigit(a);
//int bb=isdigit(b);
//for (int i=0;i<5;i++){
//	printf("%c\t%d\n",a[i],isdigit(a[i]));
//}
//printf("\n\n");
//for (int i=0;i<5;i++){
//	printf("%c\t%d\n",b[i],isdigit(b[i]));
//}
//printf("\n\n");
return 0;
}
