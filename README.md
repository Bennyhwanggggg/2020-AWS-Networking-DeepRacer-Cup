# 2020-AWS-Networking-DeepRacer-Cup
AWS Networking Organisation Internal DeepRacer Cup 2020

## Training Logs
| Training model  | Car  | reward function | Gradient descent batch size  | Number of epochs | Learning rate  | Entropy  | Discount factor  | Loss type |
| --------- |:---- |:---------------:| ----------------------------:|:---------------- |:--------------:| --------:| ---------------- |:---------:|
| v1-0    |  Bennyhwa1     | centre_line    | 512                          |              10  |   0.0003       |  0.01    |   0.999          | Huber     |
| v1-1    |  Bennyhwa1     | inside_lane_fast    | 512                          |              10  |   0.0003       |  0.01    |   0.999          | Huber     |
| v1-2    |  Bennyhwa1     | centre_line    | 256                          |              10  |   0.0001       |  0.01    |   0.999          | MSE     |
| v1-3    |  Bennyhwa1     | inside_lane_fast    | 512                          |              10  |   0.0001       |  0.01    |   0.999          | MSE     |
| v1-4    |  Bennyhwa1     | inside_lane_safety    | 512                          |              10  |   0.0001       |  0.01    |   0.999          | Huber     |
| v1-5    |  Bennyhwa1     | fast_straight_line    | 512                          |              10  |   0.0008       |  0.01    |   0.999          | Huber     |
| v1-5-1    |  Bennyhwa1     | inside_lane_faster    | 512                          |              10  |   0.0001       |  0.01    |   0.999          | MSE     |
| v2-0    |  Bennyhwa1     | deep_racer_evaluate    | 512                          |              10  |   0.0003       |  0.01    |   0.999          | Huber     |
| v2-1    |  Bennyhwa1     | deep_racer_evaluate    | 512                          |              10  |   0.0003       |  0.01    |   0.999          | Huber     |
| v1-6   |  Bennyhwa1     | deep_racer_evaluate    | 256                          |              10  |   0.0001       |  0.01    |   0.999          | Huber     |
| v2-2    |  Bennyhwa1     | centre_line    | 512                          |              10  |   0.0003       |  0.01    |   0.999          | Huber     |
| v1-5-2    |  Bennyhwa1     | inside_lane_safety    | 512                          |              10  |   0.00002       |  0.01    |   0.999          | MSE     |
| v1-5-3    |  Bennyhwa1     | inside_lane_fast    | 256                          |              10  |   0.00002       |  0.01    |   0.999          | Huber     |
| v2-3-2    |  Bennyhwa1     | inside_lane_fast    | 512                          |              10  |   0.001       |  0.01    |   0.999          | Huber     |

## Submission record
v1-3: 15.8s with 3 off-track.   
v1-4: 12.402s with 0 off-track (2nd submission one was 13.364s with 1 off-track, 1st submission was 13.5 with 1 off track, for some reason it just didn't go off track and time improved)  

## Evaluation Result
v1-3:    
1	00:00:13.056	100%	Lap complete    
2	00:00:12.508	100%	Lap complete    
3	00:00:12.360	100%	Lap complete   

v1-4:    
1	00:00:12.474	100%	Lap complete    
2	00:00:12.784	100%	Lap complete    
3	00:00:13.225	100%	Lap complete    

v1-5:  
1	00:00:12.971	100%	Lap complete    
2	00:00:13.434	100%	Lap complete    
3	00:00:13.324	100%	Lap complete    

v1-5-1:
1	00:00:01.306	2%	Off track   
2	00:00:13.252	100%	Lap complete  
3	00:00:12.946	100%	Lap complete   

v-1-5-2    
1	00:00:01.434	3%	Off track    
2	00:00:12.929	100%	Lap complete    
3	00:00:12.822	100%	Lap complete     


v2-0:    
1	00:00:06.533	50%	Off track   
2	00:00:07.065	54%	Off track  
3	00:00:12.401	100%	Lap complete  

v1-6:  
1	00:00:12.931	100%	Lap complete   
2	00:00:13.646	100%	Lap complete    
3	00:00:13.025	100%	Lap complete 

v2-1:     
1	00:00:01.240	1%	Off track
2	00:00:12.328	100%	Lap complete
3	00:00:05.561	37%	Off track

v2-2    
1	00:00:01.527	3%	Off track    
2	00:00:05.155	35%	Off track    
3	00:00:05.343	35%	Off track    


## Car Details
### The Original DeepRacer
Sensor(s): Camera.   
Neural network topology: 3 Layer CNN.   
Action space:
- Speed: 1 m/s
- Steering angle: 30°

### BennyHwa1
Sensor(s): Camera.   
Neural network topology: 3 Layer CNN.   
Action space:
- Speed: 4 m/s
- Steering angle: 30°
