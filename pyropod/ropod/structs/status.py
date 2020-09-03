
class AvailabilityStatus:
    BUSY = 0  # Executing a task
    CHARGING = 1  # Recharging its battery
    IDLE = 2  # Available (no task assigned at the moment)
    FAILURE = 3  # Critical failure, robot can't recover
    DEFECTIVE = 4  # Robot has a failure, but still functional. Requires maintenance
    NO_COMMUNICATION = 5  # FMS has lost communication with the robot for more than 15 minutes?


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
    ABORTED = 8  # Aborted by the system, not by the user
    FAILED = 1   # Execution failed
    CANCELED = 9  # Canceled before execution started
    PREEMPTED = 10  # Canceled during execution
