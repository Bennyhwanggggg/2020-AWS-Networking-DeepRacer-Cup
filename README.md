# AWS-Networking-DeepRacer-Cup-2020
AWS Networking Organisation Internal DeepRacer Cup 2020

## Training Logs
| Training model  | Car  | reward function | Gradient descent batch size  | Number of epochs | Learning rate  | Entropy  | Discount factor  | Loss type |
| --------- |:---- |:---------------:| ----------------------------:|:---------------- |:--------------:| --------:| ---------------- |:---------:|
| base 1    |  The Original DeepRacer     | centre_line    | 512                          |              10  |   0.0003       |  0.01    |   0.999          | Huber     |
| base 1    |  Bennyhwa1     | centre_line    | 512                          |              10  |   0.0003       |  0.01    |   0.999          | Huber     |
| base 1    |  Bennyhwa1     | inside_lane_fast    | 512                          |              10  |   0.0003       |  0.01    |   0.999          | Huber     |
| base 1    |  Bennyhwa1     | centre_line    | 256                          |              10  |   0.0001       |  0.01    |   0.999          | MSE     |

## Model References
base 1 - `aws-networking-internal-deepRacer-cup`


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
