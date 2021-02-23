
class AvailabilityStatus:
    BUSY = 0  # Executing a task
    CHARGING = 1  # Recharging its battery
    IDLE = 2  # Available (do not executing a task)
    FAILURE = 3  # Critical failure, can't recover
    DEFECTIVE = 4  # Has a failure, but still functional. Requires maintenance
    NO_COMMUNICATION = 5  # FMS has lost communication with the component
    RESERVED = 6  # Useful for indicating that a charging station is reserved


class ComponentStatus:
    OPTIMAL = 1
    SUBOPTIMAL = 2
    DEGRADED = 3
    CRITICAL = 4
    FAILED = 5
    NONRESPONSIVE = -1


class ActionStatus:
    PLANNED = 13
    ONGOING = 6
    COMPLETED = 2
    FAILED = 1  # Execution failed


class TaskStatus:
    UNALLOCATED = 11
    ALLOCATED = 12
    PLANNED = 13
    PLANNING_FAILED = 14
    SCHEDULED = 15  # Task is ready to be dispatched
    DISPATCHED = 16  # The task has been sent to the robot
    ONGOING = 6
    COMPLETED = 2
    OVERDUE = 3  # The task has temporal constraints in the past
    ABORTED = 8  # The task is canceled after its execution started
    FAILED = 1   # Execution failed
    CANCELED = 9  # Canceled before execution started
    DEPRECATED = 4  # Task has a deprecated format


class ElevatorRequestStatus:
    PENDING = 0
    ACCEPTED = 8
    GOING_TO_START = 1
    WAITING_FOR_ROBOT_IN = 2
    GOING_TO_GOAL = 3
    WAITING_FOR_ROBOT_OUT = 4
    COMPLETED = 5
    CANCELED = 6
    FAILED = 7
