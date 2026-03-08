Basketball Projection Prediction Project 
Section 1: Ideation
Motivation
What is your motivation?
To understand the full workflow of from coming up with a project idea to understanding its theoretical backgrounds, and to finally putting together the solution. 

Looking for the suitable dataset that fits the training  requirements for the final product. Several of these are: 
https://www.kaggle.com/datasets/energyinvestigators/projectile-motion-in-basketball/data
https://www.kaggle.com/datasets/techbaron13/nba-shots-dataset-2001-present
https://www.kaggle.com/datasets/paultimothymooney/nba-player-shooting-motions/data

What does success look like for you?
A final product where one stands before the camera and shoot a basketball, so that the UI on screen can generate lines that may predict the path of the ball. 
Scoping

My initial interest is in building a machine learning system that can predict the future trajectory of a basketball shot based on partial observations. Specifically, I want to explore how a model can take in the early portion of a ball’s flight and forecast the rest of its path, potentially even predicting whether the shot will be made or missed.
At a broader level, I am interested in trajectory prediction, computer vision, and how physics-based reasoning can be combined with deep learning. This project is motivated by applications in sports analytics, real-time feedback systems, and intelligent perception systems that interpret motion from visual data.

2. Can you get more specific? What about the technology or topic interests you?
More specifically, I am interested in the intersection of:
Sequential modeling (e.g., LSTM, Transformers) for time-series trajectory prediction


Physics-informed machine learning, where known physical laws (such as gravity and smooth motion) are incorporated into the learning process


Computer vision techniques for detecting and tracking objects (the basketball) from video


End-to-end pipelines that go from raw visual input → extracted trajectories → future motion prediction


What excites me most is not just predicting the next few points, but doing so in a way that is physically plausible, robust to noise, and interpretable. I am also interested in how uncertainty can be modeled in predictions, since real-world shots are inherently stochastic and multi-modal.

3. What domain could you apply it in?
The primary application domain is sports analytics, particularly basketball. Potential use cases include:
Real-time shot feedback for training and coaching


Automatic shot quality assessment


Player performance analysis


Augmented reality overlays showing predicted ball paths



4. What makes your idea different?
Several aspects make this project distinct from standard trajectory prediction or sports analytics approaches:
Two-Stage Learning Strategy
 Instead of relying purely on noisy video data from the start, the project first builds a strong trajectory prediction model using structured shot datasets and synthetic physics-based trajectories. A lightweight vision module is then added to bridge the gap to real-world video. This staged approach improves robustness and interpretability.


Physics-Informed Modeling
 The model will not be a black box: physical constraints (e.g., gravity consistency and trajectory smoothness) will be incorporated directly into the loss function. This differentiates the system from purely data-driven predictors.


End-to-End but Modular Design
 The pipeline is designed so that each component (detection, tracking, prediction) can be independently evaluated and improved. This allows for clearer debugging, better scientific insight, and easier extension to new domains.


Lightweight, Research-Oriented Scope
 Rather than building a large-scale commercial system, the project focuses on a compact, research-style prototype that emphasizes clarity, reproducibility, and ablation studies. This makes it suitable for a two-month timeline while still contributing meaningful technical insights.










Section 2: Project Formation
What resources might you need to start?
	
-	A suitable dataset that includes but not limited to:
Shot tracking
Ball movement data, etc.
-	Hardwares:
Camera
GPU
-	 Models:
Baseline model for linear regression
Advanced model (neural network)
Pretrained model if possible


What kind of team would you need (size, subteams, skills, onboarding)
	
Team size: 3-4 people
Skills: Machine Learning, statistical analysis, regression/classification model
How long would your project take, and what phases might you divide your time into?
	
The project will take around 2 months and we might separated it to 4 phases
Phase 1: Research and Planning (~1-2 weeks)
Phase 2: Data collection (~2 weeks)
Phase 3: Model development (~1 month)
Phase 4: Integration and Testing (~1-2 weeks)

Section 3: Project Proposals
Accurately predicting the trajectory of a basketball shot from partial observations has significant applications in sports analytics, player training, broadcast augmentation, and human–AI interaction.
Existing approaches either rely purely on physics-based models, which struggle under noisy measurements and real-world variability, or purely data-driven deep learning models, which often violate physical laws and lack interpretability.
This project aims to bridge these two paradigms by developing a physics-informed machine learning framework that can predict future basketball trajectories and shot outcomes from partial observations. The system will be designed in two stages:
Trajectory Modeling Stage: Train and evaluate models on clean, pre-collected basketball shot trajectory datasets.


Perception Integration Stage: Extend the system to real-world videos by reconstructing 3D ball trajectories from monocular camera input.
Resources (advisors, datasets, compute, etc.)
We will seek guidance from a mentor with expertise in:
Computer Vision
Machine Learning / Deep Learning
Robotics or Physics-informed Modeling
Sports Analytics
Datasets:
https://www.kaggle.com/datasets/paultimothymooney/nba-player-shooting-motions/data
https://www.kaggle.com/datasets/techbaron13/nba-shots-dataset-2001-present
https://www.kaggle.com/datasets/energyinvestigators/projectile-motion-in-basketball
Compute:
Local Compute: for debug, prepossing, 
Cloud Compute: for training
# Baketball-projection-analysis-and-prediction
