#ifdef __cplusplus
extern "C" {
#endif  /* __cplusplus */

// ----------------------------------------------------------------------------
// Color modes
// ----------------------------------------------------------------------------
#define IS_COLORMODE_INVALID                0
#define IS_COLORMODE_MONOCHROME             1
#define IS_COLORMODE_BAYER                  2
#define IS_COLORMODE_CBYCRY                 4
#define IS_COLORMODE_JPEG                   8

// ----------------------------------------------------------------------------
//  Sensor Types
// ----------------------------------------------------------------------------
#define IS_SENSOR_INVALID           0x0000

// CMOS Sensors
#define IS_SENSOR_UI141X_M          0x0001      // VGA rolling shutter, monochrome
#define IS_SENSOR_UI141X_C          0x0002      // VGA rolling shutter, color
#define IS_SENSOR_UI144X_M          0x0003      // SXGA rolling shutter, monochrome
#define IS_SENSOR_UI144X_C          0x0004      // SXGA rolling shutter, SXGA color

#define IS_SENSOR_UI154X_M          0x0030      // SXGA rolling shutter, monochrome
#define IS_SENSOR_UI154X_C          0x0031      // SXGA rolling shutter, color
#define IS_SENSOR_UI145X_C          0x0008      // UXGA rolling shutter, color

#define IS_SENSOR_UI146X_C          0x000a      // QXGA rolling shutter, color
#define IS_SENSOR_UI148X_M          0x000b      // 5MP rolling shutter, monochrome
#define IS_SENSOR_UI148X_C          0x000c      // 5MP rolling shutter, color

#define IS_SENSOR_UI121X_M          0x0010      // VGA global shutter, monochrome
#define IS_SENSOR_UI121X_C          0x0011      // VGA global shutter, VGA color
#define IS_SENSOR_UI122X_M          0x0012      // WVGA global shutter, monochrome
#define IS_SENSOR_UI122X_C          0x0013      // WVGA global shutter, color

#define IS_SENSOR_UI164X_C          0x0015      // SXGA rolling shutter, color

#define IS_SENSOR_UI155X_C          0x0017      // UXGA rolling shutter, color

#define IS_SENSOR_UI1223_M          0x0018      // WVGA global shutter, monochrome
#define IS_SENSOR_UI1223_C          0x0019      // WVGA global shutter, color

#define IS_SENSOR_UI149X_M          0x003E      // 10MP rolling shutter, monochrome
#define IS_SENSOR_UI149X_C          0x003F      // 10MP rolling shutter, color

#define IS_SENSOR_UI1225_M          0x0022      // WVGA global shutter, monochrome, LE model
#define IS_SENSOR_UI1225_C          0x0023      // WVGA global shutter, color, LE model

#define IS_SENSOR_UI1645_C          0x0025      // SXGA rolling shutter, color, LE model
#define IS_SENSOR_UI1555_C          0x0027      // UXGA rolling shutter, color, LE model
#define IS_SENSOR_UI1545_M          0x0028      // SXGA rolling shutter, monochrome, LE model
#define IS_SENSOR_UI1545_C          0x0029      // SXGA rolling shutter, color, LE model
#define IS_SENSOR_UI1455_C          0x002B      // UXGA rolling shutter, color, LE model
#define IS_SENSOR_UI1465_C          0x002D      // QXGA rolling shutter, color, LE model
#define IS_SENSOR_UI1485_M          0x002E      // 5MP rolling shutter, monochrome, LE model
#define IS_SENSOR_UI1485_C          0x002F      // 5MP rolling shutter, color, LE model
#define IS_SENSOR_UI1495_M          0x0040      // 10MP rolling shutter, monochrome, LE model
#define IS_SENSOR_UI1495_C          0x0041      // 10MP rolling shutter, color, LE model

#define IS_SENSOR_UI112X_M          0x004A      // 0768x576, HDR sensor, monochrome
#define IS_SENSOR_UI112X_C          0x004B      // 0768x576, HDR sensor, color

#define IS_SENSOR_UI1008_M          0x004C
#define IS_SENSOR_UI1008_C          0x004D

#define IS_SENSOR_UIF005_M          0x0076
#define IS_SENSOR_UIF005_C          0x0077

#define IS_SENSOR_UI1005_M          0x020A
#define IS_SENSOR_UI1005_C          0x020B

#define IS_SENSOR_UI1240_M          0x0050      // SXGA global shutter, monochrome
#define IS_SENSOR_UI1240_C          0x0051      // SXGA global shutter, color
#define IS_SENSOR_UI1240_NIR        0x0062      // SXGA global shutter, NIR

#define IS_SENSOR_UI1240LE_M        0x0054      // SXGA global shutter, monochrome, single board
#define IS_SENSOR_UI1240LE_C        0x0055      // SXGA global shutter, color, single board
#define IS_SENSOR_UI1240LE_NIR      0x0064      // SXGA global shutter, NIR, single board

#define IS_SENSOR_UI1240ML_M        0x0066      // SXGA global shutter, monochrome, single board
#define IS_SENSOR_UI1240ML_C        0x0067      // SXGA global shutter, color, single board
#define IS_SENSOR_UI1240ML_NIR      0x0200      // SXGA global shutter, NIR, single board

#define IS_SENSOR_UI1243_M_SMI      0x0078
#define IS_SENSOR_UI1243_C_SMI      0x0079

#define IS_SENSOR_UI1543_M          0x0032      // SXGA rolling shutter, monochrome, single board
#define IS_SENSOR_UI1543_C          0x0033      // SXGA rolling shutter, color, single board

#define IS_SENSOR_UI1544_M          0x003A      // SXGA rolling shutter, monochrome, single board
#define IS_SENSOR_UI1544_C          0x003B      // SXGA rolling shutter, color, single board
#define IS_SENSOR_UI1543_M_WO       0x003C      // SXGA rolling shutter, monochrome, single board
#define IS_SENSOR_UI1543_C_WO       0x003D      // SXGA rolling shutter, color, single board
#define IS_SENSOR_UI1453_C          0x0035      // UXGA rolling shutter, color, single board
#define IS_SENSOR_UI1463_C          0x0037      // QXGA rolling shutter, color, single board
#define IS_SENSOR_UI1483_M          0x0038      // QSXG rolling shutter, monochrome, single board
#define IS_SENSOR_UI1483_C          0x0039      // QSXG rolling shutter, color, single board
#define IS_SENSOR_UI1493_M          0x004E      // 10Mp rolling shutter, monochrome, single board
#define IS_SENSOR_UI1493_C          0x004F      // 10MP rolling shutter, color, single board

#define IS_SENSOR_UI1463_M_WO       0x0044      // QXGA rolling shutter, monochrome, single board
#define IS_SENSOR_UI1463_C_WO       0x0045      // QXGA rolling shutter, color, single board

#define IS_SENSOR_UI1553_C_WN       0x0047      // UXGA rolling shutter, color, single board
#define IS_SENSOR_UI1483_M_WO       0x0048      // QSXGA rolling shutter, monochrome, single board
#define IS_SENSOR_UI1483_C_WO       0x0049      // QSXGA rolling shutter, color, single board

#define IS_SENSOR_UI1580_M          0x005A      // 5MP rolling shutter, monochrome
#define IS_SENSOR_UI1580_C          0x005B      // 5MP rolling shutter, color
#define IS_SENSOR_UI1580LE_M        0x0060      // 5MP rolling shutter, monochrome, single board
#define IS_SENSOR_UI1580LE_C        0x0061      // 5MP rolling shutter, color, single board

#define IS_SENSOR_UI1360M           0x0068      // 2.2MP global shutter, monochrome
#define IS_SENSOR_UI1360C           0x0069      // 2.2MP global shutter, color
#define IS_SENSOR_UI1360NIR         0x0212      // 2.2MP global shutter, NIR

#define IS_SENSOR_UI1370M           0x006A      // 4.2MP global shutter, monochrome
#define IS_SENSOR_UI1370C           0x006B      // 4.2MP global shutter, color
#define IS_SENSOR_UI1370NIR         0x0214      // 4.2MP global shutter, NIR

#define IS_SENSOR_UI1250_M          0x006C      // 2MP global shutter, monochrome
#define IS_SENSOR_UI1250_C          0x006D      // 2MP global shutter, color
#define IS_SENSOR_UI1250_NIR        0x006E      // 2MP global shutter, NIR

#define IS_SENSOR_UI1250LE_M        0x0070      // 2MP global shutter, monochrome, single board
#define IS_SENSOR_UI1250LE_C        0x0071      // 2MP global shutter, color, single board
#define IS_SENSOR_UI1250LE_NIR      0x0072      // 2MP global shutter, NIR, single board

#define IS_SENSOR_UI1250ML_M        0x0074      // 2MP global shutter, monochrome, single board
#define IS_SENSOR_UI1250ML_C        0x0075      // 2MP global shutter, color, single board
#define IS_SENSOR_UI1250ML_NIR      0x0202      // 2MP global shutter, NIR, single board

#define IS_SENSOR_XS                0x020B      // 5MP rolling shutter, color

#define IS_SENSOR_UI1493_M_AR       0x0204
#define IS_SENSOR_UI1493_C_AR       0x0205


// CCD Sensors
#define IS_SENSOR_UI223X_M          0x0080      // Sony CCD sensor - XGA monochrome
#define IS_SENSOR_UI223X_C          0x0081      // Sony CCD sensor - XGA color

#define IS_SENSOR_UI241X_M          0x0082      // Sony CCD sensor - VGA monochrome
#define IS_SENSOR_UI241X_C          0x0083      // Sony CCD sensor - VGA color

#define IS_SENSOR_UI234X_M          0x0084      // Sony CCD sensor - SXGA monochrome
#define IS_SENSOR_UI234X_C          0x0085      // Sony CCD sensor - SXGA color

#define IS_SENSOR_UI221X_M          0x0088      // Sony CCD sensor - VGA monochrome
#define IS_SENSOR_UI221X_C          0x0089      // Sony CCD sensor - VGA color

#define IS_SENSOR_UI231X_M          0x0090      // Sony CCD sensor - VGA monochrome
#define IS_SENSOR_UI231X_C          0x0091      // Sony CCD sensor - VGA color

#define IS_SENSOR_UI222X_M          0x0092      // Sony CCD sensor - CCIR / PAL monochrome
#define IS_SENSOR_UI222X_C          0x0093      // Sony CCD sensor - CCIR / PAL color

#define IS_SENSOR_UI224X_M          0x0096      // Sony CCD sensor - SXGA monochrome
#define IS_SENSOR_UI224X_C          0x0097      // Sony CCD sensor - SXGA color

#define IS_SENSOR_UI225X_M          0x0098      // Sony CCD sensor - UXGA monochrome
#define IS_SENSOR_UI225X_C          0x0099      // Sony CCD sensor - UXGA color

#define IS_SENSOR_UI214X_M          0x009A      // Sony CCD sensor - SXGA monochrome
#define IS_SENSOR_UI214X_C          0x009B      // Sony CCD sensor - SXGA color

#define IS_SENSOR_UI228X_M          0x009C      // Sony CCD sensor - QXGA monochrome
#define IS_SENSOR_UI228X_C          0x009D      // Sony CCD sensor - QXGA color

#define IS_SENSOR_UI241X_M_R2       0x0182      // Sony CCD sensor - VGA monochrome
#define IS_SENSOR_UI251X_M          0x0182      // Sony CCD sensor - VGA monochrome
#define IS_SENSOR_UI241X_C_R2       0x0183      // Sony CCD sensor - VGA color
#define IS_SENSOR_UI251X_C          0x0183      // Sony CCD sensor - VGA color

#define IS_SENSOR_UI2130_M          0x019E      // Sony CCD sensor - WXGA monochrome
#define IS_SENSOR_UI2130_C          0x019F      // Sony CCD sensor - WXGA color

#define IS_SENSOR_PASSIVE_MULTICAST 0x0F00
// ----------------------------------------------------------------------------
// Error codes
// ----------------------------------------------------------------------------
#define IS_NO_SUCCESS                        -1   // function call failed
#define IS_SUCCESS                            0   // function call succeeded
#define IS_INVALID_CAMERA_HANDLE              1   // camera handle is not valid or zero
#define IS_INVALID_HANDLE                     1   // a handle other than the camera handle is invalid

#define IS_IO_REQUEST_FAILED                  2   // an io request to the driver failed
#define IS_CANT_OPEN_DEVICE                   3   // returned by is_InitCamera
#define IS_CANT_CLOSE_DEVICE                  4
#define IS_CANT_SETUP_MEMORY                  5
#define IS_NO_HWND_FOR_ERROR_REPORT           6
#define IS_ERROR_MESSAGE_NOT_CREATED          7
#define IS_ERROR_STRING_NOT_FOUND             8
#define IS_HOOK_NOT_CREATED                   9
#define IS_TIMER_NOT_CREATED                 10
#define IS_CANT_OPEN_REGISTRY                11
#define IS_CANT_READ_REGISTRY                12
#define IS_CANT_VALIDATE_BOARD               13
#define IS_CANT_GIVE_BOARD_ACCESS            14
#define IS_NO_IMAGE_MEM_ALLOCATED            15
#define IS_CANT_CLEANUP_MEMORY               16
#define IS_CANT_COMMUNICATE_WITH_DRIVER      17
#define IS_FUNCTION_NOT_SUPPORTED_YET        18
#define IS_OPERATING_SYSTEM_NOT_SUPPORTED    19

#define IS_INVALID_VIDEO_IN                  20
#define IS_INVALID_IMG_SIZE                  21
#define IS_INVALID_ADDRESS                   22
#define IS_INVALID_VIDEO_MODE                23
#define IS_INVALID_AGC_MODE                  24
#define IS_INVALID_GAMMA_MODE                25
#define IS_INVALID_SYNC_LEVEL                26
#define IS_INVALID_CBARS_MODE                27
#define IS_INVALID_COLOR_MODE                28
#define IS_INVALID_SCALE_FACTOR              29
#define IS_INVALID_IMAGE_SIZE                30
#define IS_INVALID_IMAGE_POS                 31
#define IS_INVALID_CAPTURE_MODE              32
#define IS_INVALID_RISC_PROGRAM              33
#define IS_INVALID_BRIGHTNESS                34
#define IS_INVALID_CONTRAST                  35
#define IS_INVALID_SATURATION_U              36
#define IS_INVALID_SATURATION_V              37
#define IS_INVALID_HUE                       38
#define IS_INVALID_HOR_FILTER_STEP           39
#define IS_INVALID_VERT_FILTER_STEP          40
#define IS_INVALID_EEPROM_READ_ADDRESS       41
#define IS_INVALID_EEPROM_WRITE_ADDRESS      42
#define IS_INVALID_EEPROM_READ_LENGTH        43
#define IS_INVALID_EEPROM_WRITE_LENGTH       44
#define IS_INVALID_BOARD_INFO_POINTER        45
#define IS_INVALID_DISPLAY_MODE              46
#define IS_INVALID_ERR_REP_MODE              47
#define IS_INVALID_BITS_PIXEL                48
#define IS_INVALID_MEMORY_POINTER            49

#define IS_FILE_WRITE_OPEN_ERROR             50
#define IS_FILE_READ_OPEN_ERROR              51
#define IS_FILE_READ_INVALID_BMP_ID          52
#define IS_FILE_READ_INVALID_BMP_SIZE        53
#define IS_FILE_READ_INVALID_BIT_COUNT       54
#define IS_WRONG_KERNEL_VERSION              55

#define IS_RISC_INVALID_XLENGTH              60
#define IS_RISC_INVALID_YLENGTH              61
#define IS_RISC_EXCEED_IMG_SIZE              62

// DirectDraw Mode errors
#define IS_DD_MAIN_FAILED                    70
#define IS_DD_PRIMSURFACE_FAILED             71
#define IS_DD_SCRN_SIZE_NOT_SUPPORTED        72
#define IS_DD_CLIPPER_FAILED                 73
#define IS_DD_CLIPPER_HWND_FAILED            74
#define IS_DD_CLIPPER_CONNECT_FAILED         75
#define IS_DD_BACKSURFACE_FAILED             76
#define IS_DD_BACKSURFACE_IN_SYSMEM          77
#define IS_DD_MDL_MALLOC_ERR                 78
#define IS_DD_MDL_SIZE_ERR                   79
#define IS_DD_CLIP_NO_CHANGE                 80
#define IS_DD_PRIMMEM_NULL                   81
#define IS_DD_BACKMEM_NULL                   82
#define IS_DD_BACKOVLMEM_NULL                83
#define IS_DD_OVERLAYSURFACE_FAILED          84
#define IS_DD_OVERLAYSURFACE_IN_SYSMEM       85
#define IS_DD_OVERLAY_NOT_ALLOWED            86
#define IS_DD_OVERLAY_COLKEY_ERR             87
#define IS_DD_OVERLAY_NOT_ENABLED            88
#define IS_DD_GET_DC_ERROR                   89
#define IS_DD_DDRAW_DLL_NOT_LOADED           90
#define IS_DD_THREAD_NOT_CREATED             91
#define IS_DD_CANT_GET_CAPS                  92
#define IS_DD_NO_OVERLAYSURFACE              93
#define IS_DD_NO_OVERLAYSTRETCH              94
#define IS_DD_CANT_CREATE_OVERLAYSURFACE     95
#define IS_DD_CANT_UPDATE_OVERLAYSURFACE     96
#define IS_DD_INVALID_STRETCH                97

#define IS_EV_INVALID_EVENT_NUMBER          100
#define IS_INVALID_MODE                     101
#define IS_CANT_FIND_FALCHOOK               102
#define IS_CANT_FIND_HOOK                   102
#define IS_CANT_GET_HOOK_PROC_ADDR          103
#define IS_CANT_CHAIN_HOOK_PROC             104
#define IS_CANT_SETUP_WND_PROC              105
#define IS_HWND_NULL                        106
#define IS_INVALID_UPDATE_MODE              107
#define IS_NO_ACTIVE_IMG_MEM                108
#define IS_CANT_INIT_EVENT                  109
#define IS_FUNC_NOT_AVAIL_IN_OS             110
#define IS_CAMERA_NOT_CONNECTED             111
#define IS_SEQUENCE_LIST_EMPTY              112
#define IS_CANT_ADD_TO_SEQUENCE             113
#define IS_LOW_OF_SEQUENCE_RISC_MEM         114
#define IS_IMGMEM2FREE_USED_IN_SEQ          115
#define IS_IMGMEM_NOT_IN_SEQUENCE_LIST      116
#define IS_SEQUENCE_BUF_ALREADY_LOCKED      117
#define IS_INVALID_DEVICE_ID                118
#define IS_INVALID_BOARD_ID                 119
#define IS_ALL_DEVICES_BUSY                 120
#define IS_HOOK_BUSY                        121
#define IS_TIMED_OUT                        122
#define IS_NULL_POINTER                     123
#define IS_WRONG_HOOK_VERSION               124
#define IS_INVALID_PARAMETER                125   // a parameter specified was invalid
#define IS_NOT_ALLOWED                      126
#define IS_OUT_OF_MEMORY                    127
#define IS_INVALID_WHILE_LIVE               128
#define IS_ACCESS_VIOLATION                 129   // an internal exception occurred
#define IS_UNKNOWN_ROP_EFFECT               130
#define IS_INVALID_RENDER_MODE              131
#define IS_INVALID_THREAD_CONTEXT           132
#define IS_NO_HARDWARE_INSTALLED            133
#define IS_INVALID_WATCHDOG_TIME            134
#define IS_INVALID_WATCHDOG_MODE            135
#define IS_INVALID_PASSTHROUGH_IN           136
#define IS_ERROR_SETTING_PASSTHROUGH_IN     137
#define IS_FAILURE_ON_SETTING_WATCHDOG      138
#define IS_NO_USB20                         139   // the usb port doesnt support usb 2.0
#define IS_CAPTURE_RUNNING                  140   // there is already a capture running

#define IS_MEMORY_BOARD_ACTIVATED           141   // operation could not execute while mboard is enabled
#define IS_MEMORY_BOARD_DEACTIVATED         142   // operation could not execute while mboard is disabled
#define IS_NO_MEMORY_BOARD_CONNECTED        143   // no memory board connected
#define IS_TOO_LESS_MEMORY                  144   // image size is above memory capacity
#define IS_IMAGE_NOT_PRESENT                145   // requested image is no longer present in the camera
#define IS_MEMORY_MODE_RUNNING              146
#define IS_MEMORYBOARD_DISABLED             147

#define IS_TRIGGER_ACTIVATED                148   // operation could not execute while trigger is enabled
#define IS_WRONG_KEY                        150
#define IS_CRC_ERROR                        151
#define IS_NOT_YET_RELEASED                 152   // this feature is not available yet
#define IS_NOT_CALIBRATED                   153   // the camera is not calibrated
#define IS_WAITING_FOR_KERNEL               154   // a request to the kernel exceeded
#define IS_NOT_SUPPORTED                    155   // operation mode is not supported
#define IS_TRIGGER_NOT_ACTIVATED            156   // operation could not execute while trigger is disabled
#define IS_OPERATION_ABORTED                157
#define IS_BAD_STRUCTURE_SIZE               158
#define IS_INVALID_BUFFER_SIZE              159
#define IS_INVALID_PIXEL_CLOCK              160
#define IS_INVALID_EXPOSURE_TIME            161
#define IS_AUTO_EXPOSURE_RUNNING            162
#define IS_CANNOT_CREATE_BB_SURF            163   // error creating backbuffer surface
#define IS_CANNOT_CREATE_BB_MIX             164   // backbuffer mixer surfaces can not be created
#define IS_BB_OVLMEM_NULL                   165   // backbuffer overlay mem could not be locked
#define IS_CANNOT_CREATE_BB_OVL             166   // backbuffer overlay mem could not be created
#define IS_NOT_SUPP_IN_OVL_SURF_MODE        167   // function not supported in overlay surface mode
#define IS_INVALID_SURFACE                  168   // surface invalid
#define IS_SURFACE_LOST                     169   // surface has been lost
#define IS_RELEASE_BB_OVL_DC                170   // error releasing backbuffer overlay DC
#define IS_BB_TIMER_NOT_CREATED             171   // backbuffer timer could not be created
#define IS_BB_OVL_NOT_EN                    172   // backbuffer overlay has not been enabled
#define IS_ONLY_IN_BB_MODE                  173   // only possible in backbuffer mode
#define IS_INVALID_COLOR_FORMAT             174   // invalid color format
#define IS_INVALID_WB_BINNING_MODE          175   // invalid binning mode for AWB
#define IS_INVALID_I2C_DEVICE_ADDRESS       176   // invalid I2C device address
#define IS_COULD_NOT_CONVERT                177   // current image couldn't be converted
#define IS_TRANSFER_ERROR                   178   // transfer failed
#define IS_PARAMETER_SET_NOT_PRESENT        179   // the parameter set is not present
#define IS_INVALID_CAMERA_TYPE              180   // the camera type in the ini file doesn't match
#define IS_INVALID_HOST_IP_HIBYTE           181   // HIBYTE of host address is invalid
#define IS_CM_NOT_SUPP_IN_CURR_DISPLAYMODE  182   // color mode is not supported in the current display mode
#define IS_NO_IR_FILTER                     183
#define IS_STARTER_FW_UPLOAD_NEEDED         184   // device starter firmware is not compatible

#define IS_DR_LIBRARY_NOT_FOUND                     185   // the DirectRender library could not be found
#define IS_DR_DEVICE_OUT_OF_MEMORY                  186   // insufficient graphics adapter video memory
#define IS_DR_CANNOT_CREATE_SURFACE                 187   // the image or overlay surface could not be created
#define IS_DR_CANNOT_CREATE_VERTEX_BUFFER           188   // the vertex buffer could not be created
#define IS_DR_CANNOT_CREATE_TEXTURE                 189   // the texture could not be created
#define IS_DR_CANNOT_LOCK_OVERLAY_SURFACE           190   // the overlay surface could not be locked
#define IS_DR_CANNOT_UNLOCK_OVERLAY_SURFACE         191   // the overlay surface could not be unlocked
#define IS_DR_CANNOT_GET_OVERLAY_DC                 192   // cannot get the overlay surface DC
#define IS_DR_CANNOT_RELEASE_OVERLAY_DC             193   // cannot release the overlay surface DC
#define IS_DR_DEVICE_CAPS_INSUFFICIENT              194   // insufficient graphics adapter capabilities
#define IS_INCOMPATIBLE_SETTING                     195   // Operation is not possible because of another incompatible setting
#define IS_DR_NOT_ALLOWED_WHILE_DC_IS_ACTIVE        196   // user App still has DC handle.
#define IS_DEVICE_ALREADY_PAIRED                    197   // The device is already paired
#define IS_SUBNETMASK_MISMATCH                      198   // The subnetmasks of the device and the adapter differ
#define IS_SUBNET_MISMATCH                          199   // The subnets of the device and the adapter differ
#define IS_INVALID_IP_CONFIGURATION                 200   // The IP configuation of the device is invalid
#define IS_DEVICE_NOT_COMPATIBLE                    201   // The device is incompatible to the driver
#define IS_NETWORK_FRAME_SIZE_INCOMPATIBLE          202   // The frame size settings of the device and the network adapter are incompatible
#define IS_NETWORK_CONFIGURATION_INVALID            203   // The network adapter configuration is invalid
#define IS_ERROR_CPU_IDLE_STATES_CONFIGURATION      204   // The setting of the CPU idle state configuration failed
#define IS_DEVICE_BUSY                              205   // The device is busy. The operation must be executed again later.
#define IS_SENSOR_INITIALIZATION_FAILED             206   // The sensor initialization failed


// ----------------------------------------------------------------------------
// common definitions
// ----------------------------------------------------------------------------
#define IS_OFF                              0
#define IS_ON                               1
#define IS_IGNORE_PARAMETER                 -1


// ----------------------------------------------------------------------------
//  device enumeration
// ----------------------------------------------------------------------------
#define IS_USE_DEVICE_ID                    0x8000L
#define IS_ALLOW_STARTER_FW_UPLOAD          0x10000L


// ----------------------------------------------------------------------------
// AutoExit enable/disable
// ----------------------------------------------------------------------------
#define IS_GET_AUTO_EXIT_ENABLED            0x8000
#define IS_DISABLE_AUTO_EXIT                0
#define IS_ENABLE_AUTO_EXIT                 1


// ----------------------------------------------------------------------------
// live/freeze parameters
// ----------------------------------------------------------------------------
#define IS_GET_LIVE                         0x8000

#define IS_WAIT                             0x0001
#define IS_DONT_WAIT                        0x0000
#define IS_FORCE_VIDEO_STOP                 0x4000
#define IS_FORCE_VIDEO_START                0x4000
#define IS_USE_NEXT_MEM                     0x8000


// ----------------------------------------------------------------------------
// video finish constants
// ----------------------------------------------------------------------------
#define IS_VIDEO_NOT_FINISH                 0
#define IS_VIDEO_FINISH                     1


// ----------------------------------------------------------------------------
// bitmap render modes
// ----------------------------------------------------------------------------
#define IS_GET_RENDER_MODE                  0x8000

#define IS_RENDER_DISABLED                  0x0000
#define IS_RENDER_NORMAL                    0x0001
#define IS_RENDER_FIT_TO_WINDOW             0x0002
#define IS_RENDER_DOWNSCALE_1_2             0x0004
#define IS_RENDER_MIRROR_UPDOWN             0x0010

#define IS_RENDER_PLANAR_COLOR_RED          0x0080
#define IS_RENDER_PLANAR_COLOR_GREEN        0x0100
#define IS_RENDER_PLANAR_COLOR_BLUE         0x0200

#define IS_RENDER_PLANAR_MONO_RED           0x0400
#define IS_RENDER_PLANAR_MONO_GREEN         0x0800
#define IS_RENDER_PLANAR_MONO_BLUE          0x1000

#define IS_RENDER_ROTATE_90                 0x0020
#define IS_RENDER_ROTATE_180                0x0040
#define IS_RENDER_ROTATE_270                0x2000

#define IS_USE_AS_DC_STRUCTURE              0x4000
#define IS_USE_AS_DC_HANDLE                 0x8000


// ----------------------------------------------------------------------------
// Trigger modes
// ----------------------------------------------------------------------------
#define IS_GET_EXTERNALTRIGGER              0x8000
#define IS_GET_TRIGGER_STATUS               0x8001
#define IS_GET_TRIGGER_MASK                 0x8002
#define IS_GET_TRIGGER_INPUTS               0x8003
#define IS_GET_SUPPORTED_TRIGGER_MODE       0x8004
#define IS_GET_TRIGGER_COUNTER              0x8000

#define IS_SET_TRIGGER_MASK                 0x0100
#define IS_SET_TRIGGER_CONTINUOUS           0x1000
#define IS_SET_TRIGGER_OFF                  0x0000
#define IS_SET_TRIGGER_HI_LO                (IS_SET_TRIGGER_CONTINUOUS | 0x0001)
#define IS_SET_TRIGGER_LO_HI                (IS_SET_TRIGGER_CONTINUOUS | 0x0002)
#define IS_SET_TRIGGER_SOFTWARE             (IS_SET_TRIGGER_CONTINUOUS | 0x0008)
#define IS_SET_TRIGGER_HI_LO_SYNC           0x0010
#define IS_SET_TRIGGER_LO_HI_SYNC           0x0020
#define IS_SET_TRIGGER_PRE_HI_LO            (IS_SET_TRIGGER_CONTINUOUS | 0x0040)
#define IS_SET_TRIGGER_PRE_LO_HI            (IS_SET_TRIGGER_CONTINUOUS | 0x0080)

#define IS_GET_TRIGGER_DELAY                0x8000
#define IS_GET_MIN_TRIGGER_DELAY            0x8001
#define IS_GET_MAX_TRIGGER_DELAY            0x8002
#define IS_GET_TRIGGER_DELAY_GRANULARITY    0x8003


// ----------------------------------------------------------------------------
// Timing
// ----------------------------------------------------------------------------

// Pixelclock
#define IS_GET_PIXEL_CLOCK                  0x8000
#define IS_GET_DEFAULT_PIXEL_CLK            0x8001
#define IS_GET_PIXEL_CLOCK_INC              0x8005

// Frame rate
#define IS_GET_FRAMERATE                    0x8000
#define IS_GET_DEFAULT_FRAMERATE            0x8001


// ----------------------------------------------------------------------------
// Gain definitions
// ----------------------------------------------------------------------------
#define IS_GET_MASTER_GAIN                  0x8000
#define IS_GET_RED_GAIN                     0x8001
#define IS_GET_GREEN_GAIN                   0x8002
#define IS_GET_BLUE_GAIN                    0x8003
#define IS_GET_DEFAULT_MASTER               0x8004
#define IS_GET_DEFAULT_RED                  0x8005
#define IS_GET_DEFAULT_GREEN                0x8006
#define IS_GET_DEFAULT_BLUE                 0x8007
#define IS_GET_GAINBOOST                    0x8008
#define IS_SET_GAINBOOST_ON                 0x0001
#define IS_SET_GAINBOOST_OFF                0x0000
#define IS_GET_SUPPORTED_GAINBOOST          0x0002
#define IS_MIN_GAIN                         0
#define IS_MAX_GAIN                         100


// ----------------------------------------------------------------------------
// Gain factor definitions
// ----------------------------------------------------------------------------
#define IS_GET_MASTER_GAIN_FACTOR           0x8000
#define IS_GET_RED_GAIN_FACTOR              0x8001
#define IS_GET_GREEN_GAIN_FACTOR            0x8002
#define IS_GET_BLUE_GAIN_FACTOR             0x8003
#define IS_SET_MASTER_GAIN_FACTOR           0x8004
#define IS_SET_RED_GAIN_FACTOR              0x8005
#define IS_SET_GREEN_GAIN_FACTOR            0x8006
#define IS_SET_BLUE_GAIN_FACTOR             0x8007
#define IS_GET_DEFAULT_MASTER_GAIN_FACTOR   0x8008
#define IS_GET_DEFAULT_RED_GAIN_FACTOR      0x8009
#define IS_GET_DEFAULT_GREEN_GAIN_FACTOR    0x800a
#define IS_GET_DEFAULT_BLUE_GAIN_FACTOR     0x800b
#define IS_INQUIRE_MASTER_GAIN_FACTOR       0x800c
#define IS_INQUIRE_RED_GAIN_FACTOR          0x800d
#define IS_INQUIRE_GREEN_GAIN_FACTOR        0x800e
#define IS_INQUIRE_BLUE_GAIN_FACTOR         0x800f


// ----------------------------------------------------------------------------
// Global Shutter definitions
// ----------------------------------------------------------------------------
#define IS_SET_GLOBAL_SHUTTER_ON            0x0001
#define IS_SET_GLOBAL_SHUTTER_OFF           0x0000
#define IS_GET_GLOBAL_SHUTTER               0x0010
#define IS_GET_SUPPORTED_GLOBAL_SHUTTER     0x0020


// ----------------------------------------------------------------------------
// Black level definitions
// ----------------------------------------------------------------------------
#define IS_GET_BL_COMPENSATION              0x8000
#define IS_GET_BL_OFFSET                    0x8001
#define IS_GET_BL_DEFAULT_MODE              0x8002
#define IS_GET_BL_DEFAULT_OFFSET            0x8003
#define IS_GET_BL_SUPPORTED_MODE            0x8004

#define IS_BL_COMPENSATION_DISABLE          0
#define IS_BL_COMPENSATION_ENABLE           1
#define IS_BL_COMPENSATION_OFFSET           32

#define IS_MIN_BL_OFFSET                    0
#define IS_MAX_BL_OFFSET                    255


// ----------------------------------------------------------------------------
// Hardware gamma definitions
// ----------------------------------------------------------------------------
#define IS_GET_HW_GAMMA                     0x8000
#define IS_GET_HW_SUPPORTED_GAMMA           0x8001
#define IS_SET_HW_GAMMA_OFF                 0x0000
#define IS_SET_HW_GAMMA_ON                  0x0001


// ----------------------------------------------------------------------------
// Image parameters
// ----------------------------------------------------------------------------

// Saturation
#define IS_GET_SATURATION_U                 0x8000
#define IS_MIN_SATURATION_U                 0
#define IS_MAX_SATURATION_U                 200
#define IS_DEFAULT_SATURATION_U             100
#define IS_GET_SATURATION_V                 0x8001
#define IS_MIN_SATURATION_V                 0
#define IS_MAX_SATURATION_V                 200
#define IS_DEFAULT_SATURATION_V             100


// ----------------------------------------------------------------------------
// Image position and size
// ----------------------------------------------------------------------------

/* Image */
#define IS_AOI_IMAGE_SET_AOI                0x0001
#define IS_AOI_IMAGE_GET_AOI                0x0002
#define IS_AOI_IMAGE_SET_POS                0x0003
#define IS_AOI_IMAGE_GET_POS                0x0004
#define IS_AOI_IMAGE_SET_SIZE               0x0005
#define IS_AOI_IMAGE_GET_SIZE               0x0006
#define IS_AOI_IMAGE_GET_POS_MIN            0x0007
#define IS_AOI_IMAGE_GET_SIZE_MIN           0x0008
#define IS_AOI_IMAGE_GET_POS_MAX            0x0009
#define IS_AOI_IMAGE_GET_SIZE_MAX           0x0010
#define IS_AOI_IMAGE_GET_POS_INC            0x0011
#define IS_AOI_IMAGE_GET_SIZE_INC           0x0012
#define IS_AOI_IMAGE_GET_POS_X_ABS          0x0013
#define IS_AOI_IMAGE_GET_POS_Y_ABS          0x0014
#define IS_AOI_IMAGE_GET_ORIGINAL_AOI       0x0015

/* Absolute position */
#define IS_AOI_IMAGE_POS_ABSOLUTE           0x10000000

/* Fast move */
#define IS_AOI_IMAGE_SET_POS_FAST           0x0020
#define IS_AOI_IMAGE_GET_POS_FAST_SUPPORTED 0x0021

/* Auto features */
#define IS_AOI_AUTO_BRIGHTNESS_SET_AOI      0x0030
#define IS_AOI_AUTO_BRIGHTNESS_GET_AOI      0x0031
#define IS_AOI_AUTO_WHITEBALANCE_SET_AOI    0x0032
#define IS_AOI_AUTO_WHITEBALANCE_GET_AOI    0x0033

/* Multi AOI */
#define IS_AOI_MULTI_GET_SUPPORTED_MODES    0x0100
#define IS_AOI_MULTI_SET_AOI                0x0200
#define IS_AOI_MULTI_GET_AOI                0x0400
#define IS_AOI_MULTI_DISABLE_AOI            0x0800
#define IS_AOI_MULTI_MODE_X_Y_AXES          0x0001
#define IS_AOI_MULTI_MODE_Y_AXES            0x0002

/* AOI sequence */
#define IS_AOI_SEQUENCE_GET_SUPPORTED       0x0050
#define IS_AOI_SEQUENCE_SET_PARAMS          0x0051
#define IS_AOI_SEQUENCE_GET_PARAMS          0x0052
#define IS_AOI_SEQUENCE_SET_ENABLE          0x0053
#define IS_AOI_SEQUENCE_GET_ENABLE          0x0054

#define IS_AOI_SEQUENCE_INDEX_AOI_1         0
#define IS_AOI_SEQUENCE_INDEX_AOI_2         1
#define IS_AOI_SEQUENCE_INDEX_AOI_3         2
#define IS_AOI_SEQUENCE_INDEX_AOI_4         4


// ----------------------------------------------------------------------------
// ROP effect constants
// ----------------------------------------------------------------------------
#define IS_GET_ROP_EFFECT                   0x8000
#define IS_GET_SUPPORTED_ROP_EFFECT         0x8001

#define IS_SET_ROP_NONE                     0
#define IS_SET_ROP_MIRROR_UPDOWN            8
#define IS_SET_ROP_MIRROR_UPDOWN_ODD        16
#define IS_SET_ROP_MIRROR_UPDOWN_EVEN       32
#define IS_SET_ROP_MIRROR_LEFTRIGHT         64


// ----------------------------------------------------------------------------
// Subsampling
// ----------------------------------------------------------------------------
#define IS_GET_SUBSAMPLING                      0x8000
#define IS_GET_SUPPORTED_SUBSAMPLING            0x8001
#define IS_GET_SUBSAMPLING_TYPE                 0x8002
#define IS_GET_SUBSAMPLING_FACTOR_HORIZONTAL    0x8004
#define IS_GET_SUBSAMPLING_FACTOR_VERTICAL      0x8008

#define IS_SUBSAMPLING_DISABLE                  0x00

#define IS_SUBSAMPLING_2X_VERTICAL              0x0001
#define IS_SUBSAMPLING_2X_HORIZONTAL            0x0002
#define IS_SUBSAMPLING_4X_VERTICAL              0x0004
#define IS_SUBSAMPLING_4X_HORIZONTAL            0x0008
#define IS_SUBSAMPLING_3X_VERTICAL              0x0010
#define IS_SUBSAMPLING_3X_HORIZONTAL            0x0020
#define IS_SUBSAMPLING_5X_VERTICAL              0x0040
#define IS_SUBSAMPLING_5X_HORIZONTAL            0x0080
#define IS_SUBSAMPLING_6X_VERTICAL              0x0100
#define IS_SUBSAMPLING_6X_HORIZONTAL            0x0200
#define IS_SUBSAMPLING_8X_VERTICAL              0x0400
#define IS_SUBSAMPLING_8X_HORIZONTAL            0x0800
#define IS_SUBSAMPLING_16X_VERTICAL             0x1000
#define IS_SUBSAMPLING_16X_HORIZONTAL           0x2000

#define IS_SUBSAMPLING_COLOR                    0x01
#define IS_SUBSAMPLING_MONO                     0x02

#define IS_SUBSAMPLING_MASK_VERTICAL            (IS_SUBSAMPLING_2X_VERTICAL | IS_SUBSAMPLING_4X_VERTICAL | IS_SUBSAMPLING_3X_VERTICAL | IS_SUBSAMPLING_5X_VERTICAL | IS_SUBSAMPLING_6X_VERTICAL | IS_SUBSAMPLING_8X_VERTICAL | IS_SUBSAMPLING_16X_VERTICAL)
#define IS_SUBSAMPLING_MASK_HORIZONTAL          (IS_SUBSAMPLING_2X_HORIZONTAL | IS_SUBSAMPLING_4X_HORIZONTAL | IS_SUBSAMPLING_3X_HORIZONTAL | IS_SUBSAMPLING_5X_HORIZONTAL | IS_SUBSAMPLING_6X_HORIZONTAL | IS_SUBSAMPLING_8X_HORIZONTAL | IS_SUBSAMPLING_16X_HORIZONTAL)


// ----------------------------------------------------------------------------
// Binning
// ----------------------------------------------------------------------------
#define IS_GET_BINNING                      0x8000
#define IS_GET_SUPPORTED_BINNING            0x8001
#define IS_GET_BINNING_TYPE                 0x8002
#define IS_GET_BINNING_FACTOR_HORIZONTAL    0x8004
#define IS_GET_BINNING_FACTOR_VERTICAL      0x8008

#define IS_BINNING_DISABLE                  0x00

#define IS_BINNING_2X_VERTICAL              0x0001
#define IS_BINNING_2X_HORIZONTAL            0x0002
#define IS_BINNING_4X_VERTICAL              0x0004
#define IS_BINNING_4X_HORIZONTAL            0x0008
#define IS_BINNING_3X_VERTICAL              0x0010
#define IS_BINNING_3X_HORIZONTAL            0x0020
#define IS_BINNING_5X_VERTICAL              0x0040
#define IS_BINNING_5X_HORIZONTAL            0x0080
#define IS_BINNING_6X_VERTICAL              0x0100
#define IS_BINNING_6X_HORIZONTAL            0x0200
#define IS_BINNING_8X_VERTICAL              0x0400
#define IS_BINNING_8X_HORIZONTAL            0x0800
#define IS_BINNING_16X_VERTICAL             0x1000
#define IS_BINNING_16X_HORIZONTAL           0x2000

#define IS_BINNING_COLOR                    0x01
#define IS_BINNING_MONO                     0x02

#define IS_BINNING_MASK_VERTICAL            (IS_BINNING_2X_VERTICAL | IS_BINNING_3X_VERTICAL | IS_BINNING_4X_VERTICAL | IS_BINNING_5X_VERTICAL | IS_BINNING_6X_VERTICAL | IS_BINNING_8X_VERTICAL | IS_BINNING_16X_VERTICAL)
#define IS_BINNING_MASK_HORIZONTAL          (IS_BINNING_2X_HORIZONTAL | IS_BINNING_3X_HORIZONTAL | IS_BINNING_4X_HORIZONTAL | IS_BINNING_5X_HORIZONTAL | IS_BINNING_6X_HORIZONTAL | IS_BINNING_8X_HORIZONTAL | IS_BINNING_16X_HORIZONTAL)


// ----------------------------------------------------------------------------
// Auto Control Parameter
// ----------------------------------------------------------------------------
#define IS_SET_ENABLE_AUTO_GAIN                     0x8800
#define IS_GET_ENABLE_AUTO_GAIN                     0x8801
#define IS_SET_ENABLE_AUTO_SHUTTER                  0x8802
#define IS_GET_ENABLE_AUTO_SHUTTER                  0x8803
#define IS_SET_ENABLE_AUTO_WHITEBALANCE             0x8804
#define IS_GET_ENABLE_AUTO_WHITEBALANCE             0x8805
#define IS_SET_ENABLE_AUTO_FRAMERATE                0x8806
#define IS_GET_ENABLE_AUTO_FRAMERATE                0x8807
#define IS_SET_ENABLE_AUTO_SENSOR_GAIN              0x8808
#define IS_GET_ENABLE_AUTO_SENSOR_GAIN              0x8809
#define IS_SET_ENABLE_AUTO_SENSOR_SHUTTER           0x8810
#define IS_GET_ENABLE_AUTO_SENSOR_SHUTTER           0x8811
#define IS_SET_ENABLE_AUTO_SENSOR_GAIN_SHUTTER      0x8812
#define IS_GET_ENABLE_AUTO_SENSOR_GAIN_SHUTTER      0x8813
#define IS_SET_ENABLE_AUTO_SENSOR_FRAMERATE         0x8814
#define IS_GET_ENABLE_AUTO_SENSOR_FRAMERATE         0x8815
#define IS_SET_ENABLE_AUTO_SENSOR_WHITEBALANCE      0x8816
#define IS_GET_ENABLE_AUTO_SENSOR_WHITEBALANCE      0x8817

#define IS_SET_AUTO_REFERENCE                       0x8000
#define IS_GET_AUTO_REFERENCE                       0x8001
#define IS_SET_AUTO_GAIN_MAX                        0x8002
#define IS_GET_AUTO_GAIN_MAX                        0x8003
#define IS_SET_AUTO_SHUTTER_MAX                     0x8004
#define IS_GET_AUTO_SHUTTER_MAX                     0x8005
#define IS_SET_AUTO_SPEED                           0x8006
#define IS_GET_AUTO_SPEED                           0x8007
#define IS_SET_AUTO_WB_OFFSET                       0x8008
#define IS_GET_AUTO_WB_OFFSET                       0x8009
#define IS_SET_AUTO_WB_GAIN_RANGE                   0x800A
#define IS_GET_AUTO_WB_GAIN_RANGE                   0x800B
#define IS_SET_AUTO_WB_SPEED                        0x800C
#define IS_GET_AUTO_WB_SPEED                        0x800D
#define IS_SET_AUTO_WB_ONCE                         0x800E
#define IS_GET_AUTO_WB_ONCE                         0x800F
#define IS_SET_AUTO_BRIGHTNESS_ONCE                 0x8010
#define IS_GET_AUTO_BRIGHTNESS_ONCE                 0x8011
#define IS_SET_AUTO_HYSTERESIS                      0x8012
#define IS_GET_AUTO_HYSTERESIS                      0x8013
#define IS_GET_AUTO_HYSTERESIS_RANGE                0x8014
#define IS_SET_AUTO_WB_HYSTERESIS                   0x8015
#define IS_GET_AUTO_WB_HYSTERESIS                   0x8016
#define IS_GET_AUTO_WB_HYSTERESIS_RANGE             0x8017
#define IS_SET_AUTO_SKIPFRAMES                      0x8018
#define IS_GET_AUTO_SKIPFRAMES                      0x8019
#define IS_GET_AUTO_SKIPFRAMES_RANGE                0x801A
#define IS_SET_AUTO_WB_SKIPFRAMES                   0x801B
#define IS_GET_AUTO_WB_SKIPFRAMES                   0x801C
#define IS_GET_AUTO_WB_SKIPFRAMES_RANGE             0x801D
#define IS_SET_SENS_AUTO_SHUTTER_PHOTOM             0x801E
#define IS_SET_SENS_AUTO_GAIN_PHOTOM                0x801F
#define IS_GET_SENS_AUTO_SHUTTER_PHOTOM             0x8020
#define IS_GET_SENS_AUTO_GAIN_PHOTOM                0x8021
#define IS_GET_SENS_AUTO_SHUTTER_PHOTOM_DEF         0x8022
#define IS_GET_SENS_AUTO_GAIN_PHOTOM_DEF            0x8023
#define IS_SET_SENS_AUTO_CONTRAST_CORRECTION        0x8024
#define IS_GET_SENS_AUTO_CONTRAST_CORRECTION        0x8025
#define IS_GET_SENS_AUTO_CONTRAST_CORRECTION_RANGE  0x8026
#define IS_GET_SENS_AUTO_CONTRAST_CORRECTION_INC    0x8027
#define IS_GET_SENS_AUTO_CONTRAST_CORRECTION_DEF    0x8028
#define IS_SET_SENS_AUTO_CONTRAST_FDT_AOI_ENABLE    0x8029
#define IS_GET_SENS_AUTO_CONTRAST_FDT_AOI_ENABLE    0x8030
#define IS_SET_SENS_AUTO_BACKLIGHT_COMP             0x8031
#define IS_GET_SENS_AUTO_BACKLIGHT_COMP             0x8032
#define IS_GET_SENS_AUTO_BACKLIGHT_COMP_RANGE       0x8033
#define IS_GET_SENS_AUTO_BACKLIGHT_COMP_INC         0x8034
#define IS_GET_SENS_AUTO_BACKLIGHT_COMP_DEF         0x8035
#define IS_SET_ANTI_FLICKER_MODE                    0x8036
#define IS_GET_ANTI_FLICKER_MODE                    0x8037
#define IS_GET_ANTI_FLICKER_MODE_DEF                0x8038
#define IS_GET_AUTO_REFERENCE_DEF                   0x8039
#define IS_GET_AUTO_WB_OFFSET_DEF                   0x803A
#define IS_GET_AUTO_WB_OFFSET_MIN                   0x803B
#define IS_GET_AUTO_WB_OFFSET_MAX                   0x803C

// ----------------------------------------------------------------------------
// Auto Control definitions
// ----------------------------------------------------------------------------
#define IS_MIN_AUTO_BRIGHT_REFERENCE          0
#define IS_MAX_AUTO_BRIGHT_REFERENCE        255
#define IS_DEFAULT_AUTO_BRIGHT_REFERENCE    128
#define IS_MIN_AUTO_SPEED                     0
#define IS_MAX_AUTO_SPEED                   100
#define IS_DEFAULT_AUTO_SPEED                50

#define IS_DEFAULT_AUTO_WB_OFFSET             0
#define IS_MIN_AUTO_WB_OFFSET               -50
#define IS_MAX_AUTO_WB_OFFSET                50
#define IS_DEFAULT_AUTO_WB_SPEED             50
#define IS_MIN_AUTO_WB_SPEED                  0
#define IS_MAX_AUTO_WB_SPEED                100
#define IS_MIN_AUTO_WB_REFERENCE              0
#define IS_MAX_AUTO_WB_REFERENCE            255


// ----------------------------------------------------------------------------
// AOI types to set/get
// ----------------------------------------------------------------------------
#define IS_SET_AUTO_BRIGHT_AOI              0x8000
#define IS_GET_AUTO_BRIGHT_AOI              0x8001
#define IS_SET_IMAGE_AOI                    0x8002
#define IS_GET_IMAGE_AOI                    0x8003
#define IS_SET_AUTO_WB_AOI                  0x8004
#define IS_GET_AUTO_WB_AOI                  0x8005


// ----------------------------------------------------------------------------
// pixel formats
// ----------------------------------------------------------------------------

/*! \brief Read current color format in function is_SetColorMode, \ref is_SetColorMode */
#define IS_GET_COLOR_MODE                   0x8000

/*! \brief Planar vs packed format */
#define IS_CM_FORMAT_PLANAR                 0x2000
#define IS_CM_FORMAT_MASK                   0x2000

/*! \brief BGR vs. RGB order */
#define IS_CM_ORDER_BGR                     0x0000
#define IS_CM_ORDER_RGB                     0x0080
#define IS_CM_ORDER_MASK                    0x0080

/*! \brief This flag indicates whether a packed source pixelformat should be used (also for the debayered pixel formats) */
#define IS_CM_PREFER_PACKED_SOURCE_FORMAT   0x4000

/*!
 * \brief Enumeration of pixel formats supported by the function is_SetColorMode, \ref is_SetColorMode.
 */

/*! \brief Raw sensor data, occupies 8 bits */
#define IS_CM_SENSOR_RAW8           11

/*! \brief Raw sensor data, occupies 16 bits */
#define IS_CM_SENSOR_RAW10          33

/*! \brief Raw sensor data, occupies 16 bits */
#define IS_CM_SENSOR_RAW12          27

/*! \brief Raw sensor data, occupies 16 bits */
#define IS_CM_SENSOR_RAW16          29

/*! \brief Mono, occupies 8 bits */
#define IS_CM_MONO8                 6

/*! \brief Mono, occupies 16 bits */
#define IS_CM_MONO10                34

/*! \brief Mono, occupies 16 bits */
#define IS_CM_MONO12                26

/*! \brief Mono, occupies 16 bits */
#define IS_CM_MONO16                28

/*! \brief BGR (5 5 5 1), 1 bit not used, occupies 16 bits */
#define IS_CM_BGR5_PACKED           (3  | IS_CM_ORDER_BGR)

/*! \brief BGR (5 6 5), occupies 16 bits */
#define IS_CM_BGR565_PACKED         (2  | IS_CM_ORDER_BGR)

/*! \brief BGR and RGB (8 8 8), occupies 24 bits */
#define IS_CM_RGB8_PACKED           (1  | IS_CM_ORDER_RGB)
#define IS_CM_BGR8_PACKED           (1  | IS_CM_ORDER_BGR)

/*! \brief BGRA and RGBA (8 8 8 8), alpha not used, occupies 32 bits */
#define IS_CM_RGBA8_PACKED          (0  | IS_CM_ORDER_RGB)
#define IS_CM_BGRA8_PACKED          (0  | IS_CM_ORDER_BGR)

/*! \brief BGRY and RGBY (8 8 8 8), occupies 32 bits */
#define IS_CM_RGBY8_PACKED          (24 | IS_CM_ORDER_RGB)
#define IS_CM_BGRY8_PACKED          (24 | IS_CM_ORDER_BGR)

/*! \brief BGR and RGB (10 10 10 2), 2 bits not used, occupies 32 bits, debayering is done from 12 bit raw */
#define IS_CM_RGB10_PACKED          (25 | IS_CM_ORDER_RGB)
#define IS_CM_BGR10_PACKED          (25 | IS_CM_ORDER_BGR)

/*! \brief BGR and RGB (10(16) 10(16) 10(16)), 6 MSB bits not used respectively, occupies 48 bits */
#define IS_CM_RGB10_UNPACKED        (35 | IS_CM_ORDER_RGB)
#define IS_CM_BGR10_UNPACKED        (35 | IS_CM_ORDER_BGR)

/*! \brief BGR and RGB (12(16) 12(16) 12(16)), 4 MSB bits not used respectively, occupies 48 bits */
#define IS_CM_RGB12_UNPACKED        (30 | IS_CM_ORDER_RGB)
#define IS_CM_BGR12_UNPACKED        (30 | IS_CM_ORDER_BGR)

/*! \brief BGRA and RGBA (12(16) 12(16) 12(16) 16), 4 MSB bits not used respectively, alpha not used, occupies 64 bits */
#define IS_CM_RGBA12_UNPACKED       (31 | IS_CM_ORDER_RGB)
#define IS_CM_BGRA12_UNPACKED       (31 | IS_CM_ORDER_BGR)

#define IS_CM_JPEG                  32

/*! \brief YUV422 (8 8), occupies 16 bits */
#define IS_CM_UYVY_PACKED           12
#define IS_CM_UYVY_MONO_PACKED      13
#define IS_CM_UYVY_BAYER_PACKED     14

/*! \brief YCbCr422 (8 8), occupies 16 bits */
#define IS_CM_CBYCRY_PACKED         23

/*! \brief RGB planar (8 8 8), occupies 24 bits */
#define IS_CM_RGB8_PLANAR           (1 | IS_CM_ORDER_RGB | IS_CM_FORMAT_PLANAR)

#define IS_CM_RGB12_PLANAR          //no compliant version
#define IS_CM_RGB16_PLANAR          //no compliant version

#define IS_CM_ALL_POSSIBLE          0xFFFF
#define IS_CM_MODE_MASK             0x007F


// ----------------------------------------------------------------------------
// Hotpixel correction
// ----------------------------------------------------------------------------
#define IS_HOTPIXEL_DISABLE_CORRECTION                  0x0000
#define IS_HOTPIXEL_ENABLE_SENSOR_CORRECTION            0x0001
#define IS_HOTPIXEL_ENABLE_CAMERA_CORRECTION            0x0002
#define IS_HOTPIXEL_ENABLE_SOFTWARE_USER_CORRECTION     0x0004
#define IS_HOTPIXEL_DISABLE_SENSOR_CORRECTION           0x0008

#define IS_HOTPIXEL_GET_CORRECTION_MODE                 0x8000
#define IS_HOTPIXEL_GET_SUPPORTED_CORRECTION_MODES      0x8001

#define IS_HOTPIXEL_GET_SOFTWARE_USER_LIST_EXISTS       0x8100
#define IS_HOTPIXEL_GET_SOFTWARE_USER_LIST_NUMBER       0x8101
#define IS_HOTPIXEL_GET_SOFTWARE_USER_LIST              0x8102
#define IS_HOTPIXEL_SET_SOFTWARE_USER_LIST              0x8103
#define IS_HOTPIXEL_SAVE_SOFTWARE_USER_LIST             0x8104
#define IS_HOTPIXEL_LOAD_SOFTWARE_USER_LIST             0x8105

#define IS_HOTPIXEL_GET_CAMERA_FACTORY_LIST_EXISTS      0x8106
#define IS_HOTPIXEL_GET_CAMERA_FACTORY_LIST_NUMBER      0x8107
#define IS_HOTPIXEL_GET_CAMERA_FACTORY_LIST             0x8108

#define IS_HOTPIXEL_GET_CAMERA_USER_LIST_EXISTS         0x8109
#define IS_HOTPIXEL_GET_CAMERA_USER_LIST_NUMBER         0x810A
#define IS_HOTPIXEL_GET_CAMERA_USER_LIST                0x810B
#define IS_HOTPIXEL_SET_CAMERA_USER_LIST                0x810C
#define IS_HOTPIXEL_GET_CAMERA_USER_LIST_MAX_NUMBER     0x810D
#define IS_HOTPIXEL_DELETE_CAMERA_USER_LIST             0x810E

#define IS_HOTPIXEL_GET_MERGED_CAMERA_LIST_NUMBER       0x810F
#define IS_HOTPIXEL_GET_MERGED_CAMERA_LIST              0x8110

#define IS_HOTPIXEL_SAVE_SOFTWARE_USER_LIST_UNICODE     0x8111
#define IS_HOTPIXEL_LOAD_SOFTWARE_USER_LIST_UNICODE     0x8112

// ----------------------------------------------------------------------------
// color correction definitions
// ----------------------------------------------------------------------------
#define IS_GET_CCOR_MODE                    0x8000
#define IS_GET_SUPPORTED_CCOR_MODE          0x8001
#define IS_GET_DEFAULT_CCOR_MODE            0x8002
#define IS_GET_CCOR_FACTOR                  0x8003
#define IS_GET_CCOR_FACTOR_MIN              0x8004
#define IS_GET_CCOR_FACTOR_MAX              0x8005
#define IS_GET_CCOR_FACTOR_DEFAULT          0x8006

#define IS_CCOR_DISABLE                     0x0000
#define IS_CCOR_ENABLE                      0x0001
#define IS_CCOR_ENABLE_NORMAL               IS_CCOR_ENABLE
#define IS_CCOR_ENABLE_BG40_ENHANCED        0x0002
#define IS_CCOR_ENABLE_HQ_ENHANCED          0x0004
#define IS_CCOR_SET_IR_AUTOMATIC            0x0080
#define IS_CCOR_FACTOR                      0x0100

#define IS_CCOR_ENABLE_MASK             (IS_CCOR_ENABLE_NORMAL | IS_CCOR_ENABLE_BG40_ENHANCED | IS_CCOR_ENABLE_HQ_ENHANCED)


// ----------------------------------------------------------------------------
// bayer algorithm modes
// ----------------------------------------------------------------------------
#define IS_GET_BAYER_CV_MODE                0x8000

#define IS_SET_BAYER_CV_NORMAL              0x0000
#define IS_SET_BAYER_CV_BETTER              0x0001
#define IS_SET_BAYER_CV_BEST                0x0002


// ----------------------------------------------------------------------------
// color converter modes
// ----------------------------------------------------------------------------
#define IS_CONV_MODE_NONE                   0x0000
#define IS_CONV_MODE_SOFTWARE               0x0001
#define IS_CONV_MODE_SOFTWARE_3X3           0x0002
#define IS_CONV_MODE_SOFTWARE_5X5           0x0004
#define IS_CONV_MODE_HARDWARE_3X3           0x0008
#define IS_CONV_MODE_OPENCL_3X3             0x0020
#define IS_CONV_MODE_OPENCL_5X5             0x0040

#define IS_CONV_MODE_JPEG                   0x0100



// ----------------------------------------------------------------------------
// Edge enhancement
// ----------------------------------------------------------------------------
#define IS_GET_EDGE_ENHANCEMENT             0x8000

#define IS_EDGE_EN_DISABLE                  0
#define IS_EDGE_EN_STRONG                   1
#define IS_EDGE_EN_WEAK                     2


// ----------------------------------------------------------------------------
// white balance modes
// ----------------------------------------------------------------------------
#define IS_GET_WB_MODE                      0x8000

#define IS_SET_WB_DISABLE                   0x0000
#define IS_SET_WB_USER                      0x0001
#define IS_SET_WB_AUTO_ENABLE               0x0002
#define IS_SET_WB_AUTO_ENABLE_ONCE          0x0004

#define IS_SET_WB_DAYLIGHT_65               0x0101
#define IS_SET_WB_COOL_WHITE                0x0102
#define IS_SET_WB_U30                       0x0103
#define IS_SET_WB_ILLUMINANT_A              0x0104
#define IS_SET_WB_HORIZON                   0x0105


// ----------------------------------------------------------------------------
// EEPROM defines
// ----------------------------------------------------------------------------
#define IS_EEPROM_MIN_USER_ADDRESS          0
#define IS_EEPROM_MAX_USER_ADDRESS          63
#define IS_EEPROM_MAX_USER_SPACE            64


// ----------------------------------------------------------------------------
// Error report modes
// ----------------------------------------------------------------------------
#define IS_GET_ERR_REP_MODE                 0x8000
#define IS_ENABLE_ERR_REP                   1
#define IS_DISABLE_ERR_REP                  0


// ----------------------------------------------------------------------------
// Display mode selectors
// ----------------------------------------------------------------------------
#define IS_GET_DISPLAY_MODE                 0x8000

#define IS_SET_DM_DIB                       1
#define IS_SET_DM_DIRECT3D                  4
#define IS_SET_DM_OPENGL                    8

#define IS_SET_DM_MONO                      0x800
#define IS_SET_DM_BAYER                     0x1000
#define IS_SET_DM_YCBCR                     0x4000


// ----------------------------------------------------------------------------
// DirectRenderer commands
// ----------------------------------------------------------------------------
#define DR_GET_OVERLAY_DC                       1
#define DR_GET_MAX_OVERLAY_SIZE                 2
#define DR_GET_OVERLAY_KEY_COLOR                3
#define DR_RELEASE_OVERLAY_DC                   4
#define DR_SHOW_OVERLAY                         5
#define DR_HIDE_OVERLAY                         6
#define DR_SET_OVERLAY_SIZE                     7
#define DR_SET_OVERLAY_POSITION                 8
#define DR_SET_OVERLAY_KEY_COLOR                9
#define DR_SET_HWND                             10
#define DR_ENABLE_SCALING                       11
#define DR_DISABLE_SCALING                      12
#define DR_CLEAR_OVERLAY                        13
#define DR_ENABLE_SEMI_TRANSPARENT_OVERLAY      14
#define DR_DISABLE_SEMI_TRANSPARENT_OVERLAY     15
#define DR_CHECK_COMPATIBILITY                  16
#define DR_SET_VSYNC_OFF                        17
#define DR_SET_VSYNC_AUTO                       18
#define DR_SET_USER_SYNC                        19
#define DR_GET_USER_SYNC_POSITION_RANGE         20
#define DR_LOAD_OVERLAY_FROM_FILE               21
#define DR_STEAL_NEXT_FRAME                     22
#define DR_SET_STEAL_FORMAT                     23
#define DR_GET_STEAL_FORMAT                     24
#define DR_ENABLE_IMAGE_SCALING                 25
#define DR_GET_OVERLAY_SIZE                     26
#define DR_CHECK_COLOR_MODE_SUPPORT             27
#define DR_GET_OVERLAY_DATA                     28
#define DR_UPDATE_OVERLAY_DATA                  29
#define DR_GET_SUPPORTED                        30

// ----------------------------------------------------------------------------
// save options
// ----------------------------------------------------------------------------
#define IS_SAVE_USE_ACTUAL_IMAGE_SIZE       0x00010000


// ----------------------------------------------------------------------------
// renumeration modes
// ----------------------------------------------------------------------------
#define IS_RENUM_BY_CAMERA                  0
#define IS_RENUM_BY_HOST                    1


// ----------------------------------------------------------------------------
// event constants
// ----------------------------------------------------------------------------
#define IS_SET_EVENT_ODD                        0
#define IS_SET_EVENT_EVEN                       1
#define IS_SET_EVENT_FRAME                      2
#define IS_SET_EVENT_EXTTRIG                    3
#define IS_SET_EVENT_VSYNC                      4
#define IS_SET_EVENT_SEQ                        5
#define IS_SET_EVENT_STEAL                      6
#define IS_SET_EVENT_VPRES                      7
#define IS_SET_EVENT_CAPTURE_STATUS             8
#define IS_SET_EVENT_TRANSFER_FAILED            IS_SET_EVENT_CAPTURE_STATUS
#define IS_SET_EVENT_DEVICE_RECONNECTED         9
#define IS_SET_EVENT_MEMORY_MODE_FINISH         10
#define IS_SET_EVENT_FRAME_RECEIVED             11
#define IS_SET_EVENT_WB_FINISHED                12
#define IS_SET_EVENT_AUTOBRIGHTNESS_FINISHED    13
#define IS_SET_EVENT_OVERLAY_DATA_LOST          16
#define IS_SET_EVENT_CAMERA_MEMORY              17
#define IS_SET_EVENT_CONNECTIONSPEED_CHANGED    18
#define IS_SET_EVENT_AUTOFOCUS_FINISHED         19
#define IS_SET_EVENT_FIRST_PACKET_RECEIVED      20
#define IS_SET_EVENT_PMC_IMAGE_PARAMS_CHANGED   21
#define IS_SET_EVENT_DEVICE_PLUGGED_IN          22
#define IS_SET_EVENT_DEVICE_UNPLUGGED           23


#define IS_SET_EVENT_REMOVE                 128
#define IS_SET_EVENT_REMOVAL                129
#define IS_SET_EVENT_NEW_DEVICE             130
#define IS_SET_EVENT_STATUS_CHANGED         131


// ----------------------------------------------------------------------------
// Window message defines
// ----------------------------------------------------------------------------
#define IS_UEYE_MESSAGE                     (WM_USER + 0x0100)
  #define IS_FRAME                          0x0000
  #define IS_SEQUENCE                       0x0001
  #define IS_TRIGGER                        0x0002
  #define IS_CAPTURE_STATUS                 0x0003
  #define IS_TRANSFER_FAILED                IS_CAPTURE_STATUS
  #define IS_DEVICE_RECONNECTED             0x0004
  #define IS_MEMORY_MODE_FINISH             0x0005
  #define IS_FRAME_RECEIVED                 0x0006
  #define IS_GENERIC_ERROR                  0x0007
  #define IS_STEAL_VIDEO                    0x0008
  #define IS_WB_FINISHED                    0x0009
  #define IS_AUTOBRIGHTNESS_FINISHED        0x000A
  #define IS_OVERLAY_DATA_LOST              0x000B
  #define IS_CAMERA_MEMORY                  0x000C
  #define IS_CONNECTIONSPEED_CHANGED        0x000D
  #define IS_AUTOFOCUS_FINISHED             0x000E
  #define IS_FIRST_PACKET_RECEIVED          0x000F
  #define IS_PMC_IMAGE_PARAMS_CHANGED       0x0010
  #define IS_DEVICE_PLUGGED_IN              0x0011
  #define IS_DEVICE_UNPLUGGED               0x0012

  #define IS_DEVICE_REMOVED                 0x1000
  #define IS_DEVICE_REMOVAL                 0x1001
  #define IS_NEW_DEVICE                     0x1002
  #define IS_DEVICE_STATUS_CHANGED          0x1003


// ----------------------------------------------------------------------------
// Camera id constants
// ----------------------------------------------------------------------------
#define IS_GET_CAMERA_ID                    0x8000


// ----------------------------------------------------------------------------
// Camera info constants
// ----------------------------------------------------------------------------
#define IS_GET_STATUS                       0x8000

#define IS_EXT_TRIGGER_EVENT_CNT            0
#define IS_FIFO_OVR_CNT                     1
#define IS_SEQUENCE_CNT                     2
#define IS_LAST_FRAME_FIFO_OVR              3
#define IS_SEQUENCE_SIZE                    4
#define IS_VIDEO_PRESENT                    5
#define IS_STEAL_FINISHED                   6
#define IS_STORE_FILE_PATH                  7
#define IS_LUMA_BANDWIDTH_FILTER            8
#define IS_BOARD_REVISION                   9
#define IS_MIRROR_BITMAP_UPDOWN             10
#define IS_BUS_OVR_CNT                      11
#define IS_STEAL_ERROR_CNT                  12
#define IS_LOW_COLOR_REMOVAL                13
#define IS_CHROMA_COMB_FILTER               14
#define IS_CHROMA_AGC                       15
#define IS_WATCHDOG_ON_BOARD                16
#define IS_PASSTHROUGH_ON_BOARD             17
#define IS_EXTERNAL_VREF_MODE               18
#define IS_WAIT_TIMEOUT                     19
#define IS_TRIGGER_MISSED                   20
#define IS_LAST_CAPTURE_ERROR               21
#define IS_PARAMETER_SET_1                  22
#define IS_PARAMETER_SET_2                  23
#define IS_STANDBY                          24
#define IS_STANDBY_SUPPORTED                25
#define IS_QUEUED_IMAGE_EVENT_CNT           26
#define IS_PARAMETER_EXT                    27


// ----------------------------------------------------------------------------
// Interface type defines
// ----------------------------------------------------------------------------
#define IS_INTERFACE_TYPE_USB               0x40
#define IS_INTERFACE_TYPE_USB3              0x60
#define IS_INTERFACE_TYPE_ETH               0x80
#define IS_INTERFACE_TYPE_PMC               0xf0


// ----------------------------------------------------------------------------
// Board type defines
// ----------------------------------------------------------------------------
#define IS_BOARD_TYPE_UEYE_USB              (IS_INTERFACE_TYPE_USB + 0)     // 0x40
#define IS_BOARD_TYPE_UEYE_USB_SE           IS_BOARD_TYPE_UEYE_USB          // 0x40
#define IS_BOARD_TYPE_UEYE_USB_RE           IS_BOARD_TYPE_UEYE_USB          // 0x40
#define IS_BOARD_TYPE_UEYE_USB_ME           (IS_INTERFACE_TYPE_USB + 0x01)  // 0x41
#define IS_BOARD_TYPE_UEYE_USB_LE           (IS_INTERFACE_TYPE_USB + 0x02)  // 0x42
#define IS_BOARD_TYPE_UEYE_USB_XS           (IS_INTERFACE_TYPE_USB + 0x03)  // 0x43
#define IS_BOARD_TYPE_UEYE_USB_ML           (IS_INTERFACE_TYPE_USB + 0x05)  // 0x45

#define IS_BOARD_TYPE_UEYE_USB3_LE          (IS_INTERFACE_TYPE_USB3 + 0x02) // 0x62
#define IS_BOARD_TYPE_UEYE_USB3_CP          (IS_INTERFACE_TYPE_USB3 + 0x04) // 0x64
#define IS_BOARD_TYPE_UEYE_USB3_ML          (IS_INTERFACE_TYPE_USB3 + 0x05) // 0x65

#define IS_BOARD_TYPE_UEYE_ETH              IS_INTERFACE_TYPE_ETH           // 0x80
#define IS_BOARD_TYPE_UEYE_ETH_HE           IS_BOARD_TYPE_UEYE_ETH          // 0x80
#define IS_BOARD_TYPE_UEYE_ETH_SE           (IS_INTERFACE_TYPE_ETH + 0x01)  // 0x81
#define IS_BOARD_TYPE_UEYE_ETH_RE           IS_BOARD_TYPE_UEYE_ETH_SE       // 0x81
#define IS_BOARD_TYPE_UEYE_ETH_LE           (IS_INTERFACE_TYPE_ETH + 0x02)  // 0x82
#define IS_BOARD_TYPE_UEYE_ETH_CP           (IS_INTERFACE_TYPE_ETH + 0x04)  // 0x84
#define IS_BOARD_TYPE_UEYE_ETH_SEP          (IS_INTERFACE_TYPE_ETH + 0x06)  // 0x86
#define IS_BOARD_TYPE_UEYE_ETH_REP          IS_BOARD_TYPE_UEYE_ETH_SEP      // 0x86
#define IS_BOARD_TYPE_UEYE_ETH_LEET         (IS_INTERFACE_TYPE_ETH + 0x07)  // 0x87
#define IS_BOARD_TYPE_UEYE_ETH_TE           (IS_INTERFACE_TYPE_ETH + 0x08)  // 0x88

// ----------------------------------------------------------------------------
// Camera type defines
// ----------------------------------------------------------------------------
#define IS_CAMERA_TYPE_UEYE_USB         IS_BOARD_TYPE_UEYE_USB_SE
#define IS_CAMERA_TYPE_UEYE_USB_SE      IS_BOARD_TYPE_UEYE_USB_SE
#define IS_CAMERA_TYPE_UEYE_USB_RE      IS_BOARD_TYPE_UEYE_USB_RE
#define IS_CAMERA_TYPE_UEYE_USB_ME      IS_BOARD_TYPE_UEYE_USB_ME
#define IS_CAMERA_TYPE_UEYE_USB_LE      IS_BOARD_TYPE_UEYE_USB_LE
#define IS_CAMERA_TYPE_UEYE_USB_ML      IS_BOARD_TYPE_UEYE_USB_ML

#define IS_CAMERA_TYPE_UEYE_USB3_LE     IS_BOARD_TYPE_UEYE_USB3_LE
#define IS_CAMERA_TYPE_UEYE_USB3_CP     IS_BOARD_TYPE_UEYE_USB3_CP
#define IS_CAMERA_TYPE_UEYE_USB3_ML     IS_BOARD_TYPE_UEYE_USB3_ML

#define IS_CAMERA_TYPE_UEYE_ETH         IS_BOARD_TYPE_UEYE_ETH_HE
#define IS_CAMERA_TYPE_UEYE_ETH_HE      IS_BOARD_TYPE_UEYE_ETH_HE
#define IS_CAMERA_TYPE_UEYE_ETH_SE      IS_BOARD_TYPE_UEYE_ETH_SE
#define IS_CAMERA_TYPE_UEYE_ETH_RE      IS_BOARD_TYPE_UEYE_ETH_RE
#define IS_CAMERA_TYPE_UEYE_ETH_LE      IS_BOARD_TYPE_UEYE_ETH_LE
#define IS_CAMERA_TYPE_UEYE_ETH_CP      IS_BOARD_TYPE_UEYE_ETH_CP
#define IS_CAMERA_TYPE_UEYE_ETH_SEP     IS_BOARD_TYPE_UEYE_ETH_SEP
#define IS_CAMERA_TYPE_UEYE_ETH_REP     IS_BOARD_TYPE_UEYE_ETH_REP
#define IS_CAMERA_TYPE_UEYE_ETH_LEET    IS_BOARD_TYPE_UEYE_ETH_LEET
#define IS_CAMERA_TYPE_UEYE_ETH_TE      IS_BOARD_TYPE_UEYE_ETH_TE
#define IS_CAMERA_TYPE_UEYE_PMC         (IS_INTERFACE_TYPE_PMC + 0x01)


// ----------------------------------------------------------------------------
// Readable operation system defines
// ----------------------------------------------------------------------------
#define IS_OS_UNDETERMINED                  0
#define IS_OS_WIN95                         1
#define IS_OS_WINNT40                       2
#define IS_OS_WIN98                         3
#define IS_OS_WIN2000                       4
#define IS_OS_WINXP                         5
#define IS_OS_WINME                         6
#define IS_OS_WINNET                        7
#define IS_OS_WINSERVER2003                 8
#define IS_OS_WINVISTA                      9
#define IS_OS_LINUX24                       10
#define IS_OS_LINUX26                       11
#define IS_OS_WIN7                          12
#define IS_OS_WIN8                          13
#define IS_OS_WIN8SERVER                    14
#define IS_OS_GREATER_THAN_WIN8             15


// ----------------------------------------------------------------------------
// Bus speed
// ----------------------------------------------------------------------------
#define IS_USB_10                           0x0001 //  1,5 Mb/s
#define IS_USB_11                           0x0002 //   12 Mb/s
#define IS_USB_20                           0x0004 //  480 Mb/s
#define IS_USB_30                           0x0008 // 4000 Mb/s
#define IS_ETHERNET_10                      0x0080 //   10 Mb/s
#define IS_ETHERNET_100                     0x0100 //  100 Mb/s
#define IS_ETHERNET_1000                    0x0200 // 1000 Mb/s
#define IS_ETHERNET_10000                   0x0400 //10000 Mb/s

#define IS_USB_LOW_SPEED                    1
#define IS_USB_FULL_SPEED                   12
#define IS_USB_HIGH_SPEED                   480
#define IS_USB_SUPER_SPEED                  4000
#define IS_ETHERNET_10Base                  10
#define IS_ETHERNET_100Base                 100
#define IS_ETHERNET_1000Base                1000
#define IS_ETHERNET_10GBase                 10000


// ----------------------------------------------------------------------------
// HDR
// ----------------------------------------------------------------------------
#define IS_HDR_NOT_SUPPORTED                0
#define IS_HDR_KNEEPOINTS                   1
#define IS_DISABLE_HDR                      0
#define IS_ENABLE_HDR                       1


// ----------------------------------------------------------------------------
// Test images
// ----------------------------------------------------------------------------
#define IS_TEST_IMAGE_NONE                          0x00000000
#define IS_TEST_IMAGE_WHITE                         0x00000001
#define IS_TEST_IMAGE_BLACK                         0x00000002
#define IS_TEST_IMAGE_HORIZONTAL_GREYSCALE          0x00000004
#define IS_TEST_IMAGE_VERTICAL_GREYSCALE            0x00000008
#define IS_TEST_IMAGE_DIAGONAL_GREYSCALE            0x00000010
#define IS_TEST_IMAGE_WEDGE_GRAY                    0x00000020
#define IS_TEST_IMAGE_WEDGE_COLOR                   0x00000040
#define IS_TEST_IMAGE_ANIMATED_WEDGE_GRAY           0x00000080

#define IS_TEST_IMAGE_ANIMATED_WEDGE_COLOR          0x00000100
#define IS_TEST_IMAGE_MONO_BARS                     0x00000200
#define IS_TEST_IMAGE_COLOR_BARS1                   0x00000400
#define IS_TEST_IMAGE_COLOR_BARS2                   0x00000800
#define IS_TEST_IMAGE_GREYSCALE1                    0x00001000
#define IS_TEST_IMAGE_GREY_AND_COLOR_BARS           0x00002000
#define IS_TEST_IMAGE_MOVING_GREY_AND_COLOR_BARS    0x00004000
#define IS_TEST_IMAGE_ANIMATED_LINE                 0x00008000

#define IS_TEST_IMAGE_ALTERNATE_PATTERN             0x00010000
#define IS_TEST_IMAGE_VARIABLE_GREY                 0x00020000
#define IS_TEST_IMAGE_MONOCHROME_HORIZONTAL_BARS    0x00040000
#define IS_TEST_IMAGE_MONOCHROME_VERTICAL_BARS      0x00080000
#define IS_TEST_IMAGE_CURSOR_H                      0x00100000
#define IS_TEST_IMAGE_CURSOR_V                      0x00200000
#define IS_TEST_IMAGE_COLDPIXEL_GRID                0x00400000
#define IS_TEST_IMAGE_HOTPIXEL_GRID                 0x00800000

#define IS_TEST_IMAGE_VARIABLE_RED_PART             0x01000000
#define IS_TEST_IMAGE_VARIABLE_GREEN_PART           0x02000000
#define IS_TEST_IMAGE_VARIABLE_BLUE_PART            0x04000000
#define IS_TEST_IMAGE_SHADING_IMAGE                 0x08000000
#define IS_TEST_IMAGE_WEDGE_GRAY_SENSOR             0x10000000
#define IS_TEST_IMAGE_ANIMATED_WEDGE_GRAY_SENSOR    0x20000000
#define IS_TEST_IMAGE_RAMPING_PATTERN               0x40000000
#define IS_TEST_IMAGE_CHESS_PATTERN                 0x80000000


// ----------------------------------------------------------------------------
// Sensor scaler
// ----------------------------------------------------------------------------
#define IS_ENABLE_SENSOR_SCALER             1
#define IS_ENABLE_ANTI_ALIASING             2


// ----------------------------------------------------------------------------
// Timeouts
// ----------------------------------------------------------------------------
#define IS_TRIGGER_TIMEOUT                  0


// ----------------------------------------------------------------------------
// Auto pixel clock modes
// ----------------------------------------------------------------------------
#define IS_BEST_PCLK_RUN_ONCE               0


// ----------------------------------------------------------------------------
// Sequence flags
// ----------------------------------------------------------------------------
#define IS_LOCK_LAST_BUFFER                 0x8002
#define IS_GET_ALLOC_ID_OF_THIS_BUF         0x8004
#define IS_GET_ALLOC_ID_OF_LAST_BUF         0x8008
#define IS_USE_ALLOC_ID                     0x8000
#define IS_USE_CURRENT_IMG_SIZE             0xC000

// ------------------------------------------
// Memory information flags
// ------------------------------------------
#define IS_GET_D3D_MEM                  0x8000


// ----------------------------------------------------------------------------
// Image files types
// ----------------------------------------------------------------------------
#define IS_IMG_BMP                          0
#define IS_IMG_JPG                          1
#define IS_IMG_PNG                          2
#define IS_IMG_RAW                          4
#define IS_IMG_TIF                          8


// ----------------------------------------------------------------------------
// I2C defines

// nRegisterAddr | IS_I2C_16_BIT_REGISTER
// nRegisterAddr | IS_I2C_0_BIT_REGISTER
// ----------------------------------------------------------------------------
#define IS_I2C_16_BIT_REGISTER          0x10000000
#define IS_I2C_0_BIT_REGISTER	        0x20000000

// nDeviceAddr | IS_I2C_DONT_WAIT
#define IS_I2C_DONT_WAIT                0x00800000


// ----------------------------------------------------------------------------
// Gamma modes
// ----------------------------------------------------------------------------
#define IS_GET_GAMMA_MODE                   0x8000
#define IS_SET_GAMMA_OFF                    0
#define IS_SET_GAMMA_ON                     1


// ----------------------------------------------------------------------------
// Capture modes   (Falcon)
// ----------------------------------------------------------------------------
#define IS_GET_CAPTURE_MODE                 0x8000

#define IS_SET_CM_ODD                       0x0001
#define IS_SET_CM_EVEN                      0x0002
#define IS_SET_CM_FRAME                     0x0004
#define IS_SET_CM_NONINTERLACED             0x0008
#define IS_SET_CM_NEXT_FRAME                0x0010
#define IS_SET_CM_NEXT_FIELD                0x0020
#define IS_SET_CM_BOTHFIELDS            (IS_SET_CM_ODD | IS_SET_CM_EVEN | IS_SET_CM_NONINTERLACED)
#define IS_SET_CM_FRAME_STEREO              0x2004


// ----------------------------------------------------------------------------
// Typedefs
// ----------------------------------------------------------------------------
#ifdef __LINUX__
        #define FORCEINLINE         inline
        #define USHORT              IS_U16

		#include <unistd.h>
        #include <wchar.h>

		#define Sleep(n)       usleep(n)

		#include <stdint.h>

        // aliases for common Win32 types
        typedef int32_t           BOOLEAN;
        typedef int32_t           BOOL;
        typedef int32_t           INT;
        typedef uint32_t          UINT;
        typedef int32_t           LONG;
        typedef void              VOID;
        typedef void*             LPVOID;
        typedef uint32_t          ULONG;

        typedef uint64_t          UINT64;
        typedef int64_t           __int64;
        typedef int64_t           LONGLONG;
        typedef uint32_t          DWORD;
        typedef uint16_t          WORD;

        typedef unsigned char     BYTE;
        typedef char              CHAR;
        typedef char              TCHAR;
        typedef unsigned char     UCHAR;

        typedef int8_t*           LPTSTR;
        typedef const int8_t*     LPCTSTR;
        typedef const int8_t*     LPCSTR;
        typedef uint32_t          WPARAM;
        typedef uint32_t          LPARAM;
        typedef uint32_t          LRESULT;
        typedef uint32_t          HRESULT;

        typedef void*             HWND;
        typedef void*             HGLOBAL;
        typedef void*             HINSTANCE;
        typedef void*             HDC;
        typedef void*             HMODULE;
        typedef void*             HKEY;
        typedef void*             HANDLE;

        typedef BYTE*             LPBYTE;
        typedef DWORD*            PDWORD;
        typedef VOID*             PVOID;
        typedef CHAR*             PCHAR;



    #ifndef FALSE
        #define FALSE 0
    #endif
    #ifndef TRUE
        #define TRUE 1
    #endif

    #ifndef HIBYTE
        #define HIBYTE(_x_)    ( (_x_)>>8 )
    #endif

    #ifndef LOBYTE
        #define LOBYTE(_x_)    ( (_x_)&0x00ff )
    #endif

    #ifndef HIWORD
        #define HIWORD(_x_)    ( (_x_)>>16 )
    #endif

    #ifndef LOWORD
        #define LOWORD(_x_)    ( (_x_)&0x0000ffff )
    #endif

    #ifndef _min_
        #define _min_( _x_, _y_ ) ( (_x_)<(_y_) ? (_x_) : (_y_) )
    #endif

    #ifndef _max_
        #define _max_( _x_, _y_ ) ( (_x_)>(_y_) ? (_x_) : (_y_) )
    #endif

    #ifndef WM_USER
        #define WM_USER        0x400
    #endif

        // unknown stuff for Linux
        #define WINAPI
        #define CALLBACK
        #undef  UNICODE
        #define __stdcall
        #define __cdecl
#if defined __i386__
        #define IDSEXP    __attribute__((cdecl)) INT
        #define IDSEXPUL  __attribute__((cdecl)) ULONG
#else
        #define IDSEXP    INT
        #define IDSEXPUL  ULONG
#endif



    #define ZeroMemory(a,b)      memset((a), 0, (b))
    #define OutputDebugString(s) fprintf(stderr, s)


    #define INFINITE    -1
#else

#include <windows.h>
typedef int     INT;

#ifdef _WIN32_WCE
  typedef TCHAR IS_CHAR;
#else
  typedef char IS_CHAR;
#endif


// ----------------------------------------------------------------------------
// Typedefs
// ----------------------------------------------------------------------------
typedef DWORD   HIDS;
#define HIDS_DEFINED

typedef DWORD   HCAM;
#define HCAM_DEFINED

typedef DWORD   HFALC;
#define HFALC_DEFINED


// ----------------------------------------------------------------------------
// Invalid values for device handles
// ----------------------------------------------------------------------------
#define IS_INVALID_HIDS (HIDS)0
#define IS_INVALID_HCAM (HIDS)0
#define IS_INVALID_HFALC (HIDS)0

// ----------------------------------------------------------------------------
// Auto feature structs and definitions
// ----------------------------------------------------------------------------
#define AC_SHUTTER                          0x00000001
#define AC_GAIN                             0x00000002
#define AC_WHITEBAL                         0x00000004
#define AC_WB_RED_CHANNEL                   0x00000008
#define AC_WB_GREEN_CHANNEL                 0x00000010
#define AC_WB_BLUE_CHANNEL                  0x00000020
#define AC_FRAMERATE                        0x00000040
#define AC_SENSOR_SHUTTER                   0x00000080
#define AC_SENSOR_GAIN                      0x00000100
#define AC_SENSOR_GAIN_SHUTTER              0x00000200
#define AC_SENSOR_FRAMERATE                 0x00000400
#define AC_SENSOR_WB                        0x00000800
#define AC_SENSOR_AUTO_REFERENCE            0x00001000
#define AC_SENSOR_AUTO_SPEED                0x00002000
#define AC_SENSOR_AUTO_HYSTERESIS           0x00004000
#define AC_SENSOR_AUTO_SKIPFRAMES           0x00008000
#define AC_SENSOR_AUTO_CONTRAST_CORRECTION  0x00010000
#define AC_SENSOR_AUTO_CONTRAST_FDT_AOI     0x00020000
#define AC_SENSOR_AUTO_BACKLIGHT_COMP       0x00040000

#define ACS_ADJUSTING 0x00000001
#define ACS_FINISHED  0x00000002
#define ACS_DISABLED  0x00000004


#ifdef __cplusplus
};
#endif  /* __cplusplus */


#endif  // #ifndef __IDS_HEADER__
