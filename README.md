ComfyUI DynamiCrafter

[DynamiCrafter](https://github.com/Doubiiu/DynamiCrafter)

注意一定要安装xformers `pip install xformers`

## Examples

### base workflow

<img src="wf-basic.png" raw=true>

https://github.com/chaojie/ComfyUI-DynamiCrafter/blob/main/workflow.json

prompt: 1girl

<img src="video.gif" raw=true>

prompt: 1girl sleeping

<img src="1girl_sleeping.gif" raw=true>

4090 test:

16 frame length takes 3 minutes

32 frame length takes 6 minutes (32设置是在Loader节点)



### interpolation workflow

<img src="wf-interp.png" raw=true>

https://github.com/chaojie/ComfyUI-DynamiCrafter/blob/main/wf-interp.json