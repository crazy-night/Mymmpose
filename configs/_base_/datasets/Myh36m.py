dataset_info = dict(
    dataset_name='Myh36m',
    paper_info=dict(
        author='Ionescu, Catalin and Papava, Dragos and '
        'Olaru, Vlad and Sminchisescu, Cristian',
        title='Human3.6M: Large Scale Datasets and Predictive '
        'Methods for 3D Human Sensing in Natural Environments',
        container='IEEE Transactions on Pattern Analysis and '
        'Machine Intelligence',
        year='2014',
        homepage='http://vision.imar.ro/human3.6m/description.php',
    ),
    keypoint_info={
        0:
        dict(name='root', id=0, color=[51, 153, 255], type='lower', swap=''),
        1:
        dict(
            name='right_hip',
            id=1,
            color=[255, 128, 0],
            type='lower',
            swap='left_hip'),
        2:
        dict(
            name='right_knee',
            id=2,
            color=[255, 128, 0],
            type='lower',
            swap='left_knee'),
        3:
        dict(
            name='right_foot',
            id=3,
            color=[255, 128, 0],
            type='lower',
            swap='left_foot'),
        4:
        dict(
            name='right_toe',
            id=4,
            color=[255, 128, 0],
            type='lower',
            swap='left_toe'),    
        5:
        dict(
            name='left_hip',
            id=5,
            color=[0, 255, 0],
            type='lower',
            swap='right_hip'),
        6:
        dict(
            name='left_knee',
            id=6,
            color=[0, 255, 0],
            type='lower',
            swap='right_knee'),
        7:
        dict(
            name='left_foot',
            id=7,
            color=[0, 255, 0],
            type='lower',
            swap='right_foot'),
        8:
        dict(
            name='left_toe',
            id=8,
            color=[0, 255, 0],
            type='lower',
            swap='right_toe'),    
        9:
        dict(name='spine', id=9, color=[51, 153, 255], type='upper', swap=''),
        10:
        dict(name='thorax', id=10, color=[51, 153, 255], type='upper', swap=''),
        11:
        dict(
            name='neck_base',
            id=11,
            color=[51, 153, 255],
            type='upper',
            swap=''),
        12:
        dict(name='head', id=12, color=[51, 153, 255], type='upper', swap=''),
        13:
        dict(
            name='left_shoulder',
            id=13,
            color=[0, 255, 0],
            type='upper',
            swap='right_shoulder'),
        14:
        dict(
            name='left_elbow',
            id=14,
            color=[0, 255, 0],
            type='upper',
            swap='right_elbow'),
        15:
        dict(
            name='left_wrist',
            id=15,
            color=[0, 255, 0],
            type='upper',
            swap='right_wrist'),
        16:
        dict(
            name='right_shoulder',
            id=16,
            color=[255, 128, 0],
            type='upper',
            swap='left_shoulder'),
        17:
        dict(
            name='right_elbow',
            id=17,
            color=[255, 128, 0],
            type='upper',
            swap='left_elbow'),
        18:
        dict(
            name='right_wrist',
            id=18,
            color=[255, 128, 0],
            type='upper',
            swap='left_wrist')
    },
    skeleton_info={
        0:
        dict(link=('root', 'right_hip'), id=0, color=[255, 128, 0]),
        1:
        dict(link=('right_hip', 'right_knee'), id=1, color=[255, 128, 0]),
        2:
        dict(link=('right_knee', 'right_foot'), id=2, color=[255, 128, 0]),
        3:
        dict(link=('right_foot', 'right_toe'), id=3, color=[255, 128, 0]),
        4:
        dict(link=('root', 'left_hip'), id=4, color=[0, 255, 0]),
        5:
        dict(link=('left_hip', 'left_knee'), id=5, color=[0, 255, 0]),
        6:
        dict(link=('left_knee', 'left_foot'), id=6, color=[0, 255, 0]),
        7:
        dict(link=('left_foot', 'left_toe'), id=7, color=[0, 255, 0]),
        8:
        dict(link=('root', 'spine'), id=8, color=[51, 153, 255]),
        9:
        dict(link=('spine', 'thorax'), id=9, color=[51, 153, 255]),
        10:
        dict(link=('thorax', 'neck_base'), id=10, color=[51, 153, 255]),
        11:
        dict(link=('neck_base', 'head'), id=11, color=[51, 153, 255]),
        12:
        dict(link=('thorax', 'right_shoulder'), id=12, color=[255, 128, 0]),
        13:
        dict(link=('right_shoulder', 'right_elbow'), id=13, color=[255, 128, 0]),
        14:
        dict(link=('right_elbow', 'right_wrist'), id=14, color=[255, 128, 0]),
        15:
        dict(link=('thorax', 'left_shoulder'), id=15, color=[0, 255, 0]),
        16:
        dict(link=('left_shoulder', 'left_elbow'), id=16, color=[0, 255, 0]),
        17:
        dict(link=('left_elbow', 'left_wrist'), id=17, color=[0, 255, 0])
    },
    joint_weights=[1.] * 19,
    sigmas=[0.01] * 19,
    stats_info=dict(bbox_center=(528., 427.), bbox_scale=400.))
