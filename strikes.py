import math

def euclidian( point1, point2):
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 )

def angle_calc(p0, p1, p2 ):
    '''
        p1 is center point from where we measured angle between p0 and p2
    '''
    try:
        a = (p1[0]-p0[0])**2 + (p1[1]-p0[1])**2
        b = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
        c = (p2[0]-p0[0])**2 + (p2[1]-p0[1])**2
        angle = math.acos( (a+b-c) / math.sqrt(4*a*b) ) * 180/math.pi
    except:
        return 0
    return int(angle)

def strike(part_line):
	label = 'UNKOWN STRIKE'
	if 11 in part_line and 12 in part_line and 13 in part_line and 14 in part_line and 15 in part_line and 16 in part_line and 23 in part_line and 24 in part_line:

		r_arm_angle = angle_calc(part_line[12], part_line[14], part_line[16])
		l_arm_angle = angle_calc(part_line[11], part_line[13], part_line[15])
		angle_Rsh_Lsh_Lel = angle_calc(part_line[12], part_line[11], part_line[13])

		dis_Rw_Lsh = euclidian(part_line[16], part_line[11]) # right wrist to left shoulder
		dis_Lw_Rsh = euclidian(part_line[15], part_line[12]) # left wrist to right shoulder
		dis_Rw_Rsh = euclidian(part_line[16], part_line[12]) # right wrist to right shoulder
		dis_Lw_Lsh = euclidian(part_line[15], part_line[11]) # left wrist to left shoulder
		dis_Lw_Lhip = euclidian(part_line[15], part_line[23]) # left wrist to left hip
		dis_Rw_Rhip = euclidian(part_line[16], part_line[24]) # right wrist to right hip
		dis_Rw_nose = euclidian(part_line[16], part_line[0]) # right wrist to nose
		dis_Lw_nose = euclidian(part_line[15], part_line[0]) # left wrist to nose

		# Pugay
		if r_arm_angle < 70 and l_arm_angle >= 140 and dis_Rw_Lsh < dis_Rw_Rsh and angle_Rsh_Lsh_Lel > 90:
			label = 'PUGAY'

		# Handa
		elif r_arm_angle > 160 and l_arm_angle >= 140 and dis_Rw_Lsh > dis_Rw_Rsh and angle_Rsh_Lsh_Lel > 90:
			label = 'HANDA'

		# Left temple
		elif (
				r_arm_angle < 45 and l_arm_angle >= 140 and dis_Rw_Lsh > dis_Rw_Rsh and angle_Rsh_Lsh_Lel > 90 and dis_Lw_Lsh < dis_Lw_Lhip) or \
				(
						r_arm_angle < 100 and l_arm_angle <= 90 and dis_Rw_Lsh < dis_Rw_Rsh and angle_Rsh_Lsh_Lel > 90 and dis_Lw_Lsh < dis_Lw_Lhip):
			label = 'Left Temple'

		# Right temple
		elif (
				r_arm_angle > 100 and l_arm_angle >= 140 and dis_Rw_Lsh < dis_Rw_Rsh and angle_Rsh_Lsh_Lel < 100 and dis_Lw_Lsh < dis_Lw_Lhip) or \
				(
						r_arm_angle < 100 and l_arm_angle <= 90 and dis_Rw_Lsh > dis_Rw_Rsh and angle_Rsh_Lsh_Lel > 90 and dis_Lw_Lsh < dis_Lw_Lhip):
			label = 'Right Temple'

		# Left Shoulder
		elif (
				r_arm_angle < 90 and l_arm_angle >= 140 and dis_Rw_Lsh > dis_Rw_Rsh and angle_Rsh_Lsh_Lel > 90 and dis_Lw_Lsh < dis_Lw_Lhip) or \
				(
						r_arm_angle < 60 and l_arm_angle <= 90 and dis_Rw_Lsh > dis_Rw_Rsh and angle_Rsh_Lsh_Lel > 90 and dis_Lw_Lsh < dis_Lw_Lhip):
			label = 'Left Shoulder'

		# Right Shoulder
		elif (
				r_arm_angle > 90 and l_arm_angle < 45 and dis_Rw_Lsh < dis_Rw_Rsh and angle_Rsh_Lsh_Lel > 90 and dis_Lw_Lsh < dis_Lw_Lhip) or \
				(
						r_arm_angle < 60 and l_arm_angle <= 90 and dis_Rw_Lsh < dis_Rw_Rsh and angle_Rsh_Lsh_Lel > 90 and dis_Lw_Lsh < dis_Lw_Lhip):
			label = 'Right Shoulder'

		# Stomach Thrust
		elif (
				r_arm_angle > 100 and l_arm_angle < 45 and dis_Rw_Lsh > dis_Rw_Rsh and angle_Rsh_Lsh_Lel > 90 and dis_Lw_Lsh < dis_Lw_Lhip) or \
				(
						r_arm_angle > 100 and l_arm_angle <= 90 and dis_Rw_Lsh > dis_Rw_Rsh and angle_Rsh_Lsh_Lel > 90 and dis_Lw_Lsh < dis_Lw_Lhip):
			label = 'Stomach Thrust'

		# Left chest
		elif (
				r_arm_angle < 90 and l_arm_angle > 80 and dis_Rw_Lsh > dis_Rw_Rsh and angle_Rsh_Lsh_Lel > 120 and dis_Lw_Lsh < dis_Lw_Lhip) or \
				(
						r_arm_angle > 100 and l_arm_angle <= 90 and dis_Rw_Lsh > dis_Rw_Rsh and angle_Rsh_Lsh_Lel < 90 and dis_Lw_Lsh < dis_Lw_Lhip):
			label = 'Left Chest'

		# Right chest
		elif (
				r_arm_angle > 100 and l_arm_angle < 45 and dis_Rw_Lsh < dis_Rw_Rsh and angle_Rsh_Lsh_Lel > 120 and dis_Lw_Lsh < dis_Lw_Lhip) or \
				(
						r_arm_angle > 100 and l_arm_angle <= 90 and dis_Rw_Lsh < dis_Rw_Rsh and angle_Rsh_Lsh_Lel > 100 and dis_Lw_Lsh < dis_Lw_Lhip):
			label = 'Right Chest'

		# Left knee
		elif (
				r_arm_angle < 45 and l_arm_angle < 45 and dis_Rw_Lsh > dis_Rw_Rsh and angle_Rsh_Lsh_Lel > 100 and dis_Lw_Lsh < dis_Lw_Lhip) or \
				(
						r_arm_angle > 160 and l_arm_angle <= 90 and dis_Rw_Lsh > dis_Rw_Rsh and angle_Rsh_Lsh_Lel > 100 and dis_Lw_Lsh < dis_Lw_Lhip):
			label = 'Left Knee'

		# Right knee
		elif (
				r_arm_angle < 45 and l_arm_angle < 45 and dis_Rw_Lsh < dis_Rw_Rsh and angle_Rsh_Lsh_Lel > 100 and dis_Lw_Lsh < dis_Lw_Lhip) or \
				(
						r_arm_angle > 160 and l_arm_angle <= 90 and dis_Rw_Lsh > dis_Rw_Rsh and angle_Rsh_Lsh_Lel > 100 and dis_Lw_Lsh < dis_Lw_Lhip):
			label = 'Right Knee'

		# Left eye
		elif (
				r_arm_angle < 90 and l_arm_angle > 100 and dis_Rw_Lsh > dis_Rw_Rsh and angle_Rsh_Lsh_Lel < 45 and dis_Lw_Lsh < dis_Lw_Lhip) or \
				(
						r_arm_angle > 160 and l_arm_angle <= 90 and dis_Rw_Lsh > dis_Rw_Rsh and angle_Rsh_Lsh_Lel < 90 and dis_Lw_Lsh < dis_Lw_Lhip):
			label = 'Left Eye'

		# Right eye

		# Crown
		elif (
				r_arm_angle < 45 and l_arm_angle > 160 and dis_Rw_Lsh > dis_Rw_Rsh and angle_Rsh_Lsh_Lel < 90 and dis_Lw_Lsh < dis_Lw_Lhip) or \
				(
						r_arm_angle < 45 and l_arm_angle <= 50 and dis_Rw_Lsh > dis_Rw_Rsh and angle_Rsh_Lsh_Lel > 90 and dis_Lw_Lsh < dis_Lw_Lhip):
			label = 'Crown'

	else:
		label = 'Keypoints undetected'

	# print('  ', l_arm_angle, r_arm_angle, angle_Rsh_Lsh_Lel)
	# print('  ', dis_Lw_Lsh, dis_Rw_Rsh, dis_Rw_Lsh, dis_Lw_Lhip)

	if label == 'UNKOWN STRIKE':
		if dis_Rw_Lsh < dis_Rw_Rsh and dis_Rw_nose > dis_Lw_nose:
			label = 'Left Upper Body Block'

		elif dis_Rw_Lsh > dis_Rw_Rsh and dis_Rw_nose > dis_Lw_nose and dis_Rw_Rhip < dis_Rw_nose:
			label = 'Right Upper Body Block'

		elif dis_Rw_nose < dis_Lw_nose:
			label = 'Stomach Thrust Block'

		elif dis_Rw_nose < dis_Rw_Rsh and dis_Lw_nose < dis_Lw_Lsh:
			label = 'Rising Block'

	return label


		


def joint_angles(part_line):
	r_elbow = 0
	l_elbow = 0
	r_shoulder = 0
	l_shoulder = 0
	r_hip = 0
	l_hip = 0
	r_knee = 0
	l_knee = 0


	if 12 in part_line and 14 in part_line and 16 in part_line:
		r_elbow = angle_calc(part_line[12], part_line[14], part_line[16])

	if 11 in part_line and 13 in part_line and 15 in part_line:
		l_elbow = angle_calc(part_line[11], part_line[13], part_line[15])

	if 11 in part_line and 12 in part_line and 14 in part_line:
		r_shoulder = angle_calc(part_line[11], part_line[12], part_line[14])

	if 12 in part_line and 11 in part_line and 13 in part_line:
		l_shoulder = angle_calc(part_line[12], part_line[11], part_line[13])

	if 26 in part_line and 24 in part_line and 23 in part_line:
		r_hip = angle_calc(part_line[26], part_line[24], part_line[23])

	if 25 in part_line and 23 in part_line and 24 in part_line:
		l_hip = angle_calc(part_line[25], part_line[23], part_line[24])

	if 24 in part_line and 26 in part_line and 28 in part_line:
		r_knee = angle_calc(part_line[24], part_line[26], part_line[28])

	if 23 in part_line and 25 in part_line and 27 in part_line:
		l_knee = angle_calc(part_line[23], part_line[25], part_line[27])

	angle_dict = {'right elbow': r_elbow, 'left elbow': l_elbow, 'right shoulder': r_shoulder, 'left shoulder': l_shoulder, 
	'right hip': r_hip, 'left hip': l_hip, 'right knee': r_knee, 'left knee': l_knee
	}

	return angle_dict