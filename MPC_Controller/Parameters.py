from MPC_Controller.utils import GaitType, FSM_OperatingMode, FSM_StateName


class Parameters:
    cmpc_x_drag = 3.0
    cmpc_bonus_swing = 0.0
    cmpc_alpha = 4e-5
    
    cmpc_print_solver_time = False
    cmpc_print_total_time = False

    cmpc_py_solver = 1 # 0 cvxopt, 1 osqp
    cmpc_solver_type = 2 # 0 my py solver, 1 mit cpp solver, 2 google cpp solver
    cmpc_gait = GaitType.TROT # 1 bound, 2 pronk, 3 pace, 4 stand, else trot

    control_mode = FSM_StateName.PASSIVE # 0 passive, 4 locomotion, 6 recovery stand
    operatingMode = FSM_OperatingMode.NORMAL # 0 no transition and safe check, 1 normal
    controller_dt = 0.01 # 100 Hz

    locomotionUnsafe = False # global indicator for switching contorl mode