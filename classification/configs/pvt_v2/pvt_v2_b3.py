cfg = dict(
    model='pvt_v2_b3',
    drop_path=0.3,
    clip_grad=1.0,
    output_dir='checkpoints/pvt_v2_b3_pretrained',
    data_set='Chaoyang',
    data_path='./datasets/chaoyang/',
    batch_size=12,
)
