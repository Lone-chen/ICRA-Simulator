def change_location(self, l_v, angle_v):
    """
    :param l_v: 小车的线速度
    :param angle_v: 小车的角速度
    :return:
    """
    t = (angle_v - self.angular_speed) / self.angular_acel
    t_ = (l_v - self.line_speed) / self.line_acel
    # 角速度线速度到目标速度所需时间大于帧
    if t > self.T and t_ > self.T:
        v_x = (self.line_speed + self.line_acel * self.T) * math.cos(self.angle) * math.cos(
            self.angle + self.angular_speed * self.T
            + self.angular_acel * self.T * self.T / 2) - (self.line_speed + self.line_acel * self.T) * math.sin(
            self.angle) * math.sin \
                  (self.angle + self.angular_speed * self.T + self.angular_acel * self.T * self.T / 2)

        v_y = (self.line_speed + self.line_acel * self.T) * math.sin(self.angle) * math.sin(
            self.angle + self.angular_speed * self.T
            + self.angular_acel * self.T * self.T / 2) + (self.line_speed + self.line_acel * self.T) * math.cos(
            self.angle) * math.cos \
                  (self.angle + self.angular_speed * self.T + self.angular_acel * self.T * self.T / 2)
        self.angular_speed = self.angular_speed + self.angular_acel * self.T
        self.angle = self.angle + self.angular_speed * self.T
        x =
        y =
        self.line_speed = math.sqrt(v_x * v_x + v_y * v_y)
        # 积分求位移

    # 角速度到目标速度所需时间小于帧，线速度到目标速度时间大于帧
    elif t <= self.T and t_ > self.T:
        angle = self.angle + (angle_v * angle_v - self.angular_speed * self.angular_speed) / (2 * self.angular_acel) + \
                self.angular_speed * (self.T - (angle_v - self.angular_speed) / self.angular_acel)
        v_x = (self.line_speed + self.line_acel * self.T) * math.cos(self.angle) * math.cos(angle) - \
              (self.line_speed + self.line_acel * self.T) * math.sin(self.angle) * math.sin(angle)

        v_y = (self.line_speed + self.line_acel * self.T) * math.sin(self.angle) * math.sin(angle) + \
              (self.line_speed + self.line_acel * self.T) * math.cos(self.angle) * math.cos(angle)
        self.angular_speed = angle_v
        self.angle = self.angle + self.angular_speed * t / 2 + angle_v * (self.T - t)
        x =
        y =
        self.line_speed = math.sqrt(v_x * v_x + v_y * v_y)
        # 积分求位移


    # 角速度到目标速度时间大于帧，线速度到目标速度所需时间小于帧
    elif t > self.T and t_ <= self.T：
    # 加速到线速度达到目标速度时的速度
    v_x = (self.line_speed + self.line_acel * t_) * math.cos(self.angle) * math.cos(
        self.angle + self.angular_speed * t_ + \
        self.angular_acel * t_ * t_ / 2) - (self.line_speed + self.line_acel * t_) * math.sin(
        self.angle) * math.sin(self.angle + self.angular_speed * t_ + self.angular_acel * t_ * t_ / 2)

    v_y = (self.line_speed + self.line_acel * t_) * math.sin(self.angle) * math.sin(self.angle + self.angular_speed * t_
                                                                                    + self.angular_acel * t_ * t_ / 2) + (
                      self.line_speed + self.line_acel * t_) * math.cos(
        self.angle) * math.cos(self.angle + self.angular_speed * t_ + self.angular_acel * t_ * t_ / 2)
    self.line_speed = l_v
    self.angle += self.angular_speed * t_ + self.angular_acel * t_ * t_ / 2
    self.angular_speed += self.angular_acel * t_
    x =
    y =
    # 速度恒定，角速度继续增加
    v_x = (self.line_speed) * math.cos(self.angle) * math.cos(self.angle + self.angular_speed * (self.T - t_) + \
                                                              self.angular_acel * (self.T - t_) * (self.T - t_) / 2) - (
              self.line_speed) * math.sin(
        self.angle) * math.sin(self.angle + self.angular_speed * (self.T - t_) + \
                               self.angular_acel * (self.T - t_) * (self.T - t_) / 2)

    v_y = (self.line_speed) * math.sin(self.angle) * math.sin(self.angle + self.angular_speed * (self.T - t_) + \
                                                              self.angular_acel * (self.T - t_) * (self.T - t_) / 2) + (
              self.line_speed) * math.cos(self.angle) * math.cos(self.angle + self.angular_speed * (self.T - t_) + \
                                                                 self.angular_acel * (self.T - t_) * (self.T - t_) / 2)
    x +=
    y +=
    self.angle += self.angular_speed * (self.T - t_) + self.angular_acel * (self.T - t_) * (self.T - t_) / 2
    self.angular_speed = self.angular_speed + self.angular_acel * (self.T - t_)

# 角速度到目标速度时间小于帧，线速度到目标速度所需时间小于帧
elif t <= self.T and t_ <= self.T:
if t < t_:
    v_x = (self.line_speed + self.line_acel * t) * math.cos(self.angle) * \
          math.cos(self.angle + self.angular_speed * t + self.angular_acel * t * t / 2) - \
          (self.line_speed + self.line_acel * t) * math.sin(self.angle) * \
          math.sin(self.angle + self.angular_speed * t + self.angular_acel * t * t / 2)

    v_y = (self.line_speed + self.line_acel * t) * math.sin(self.angle) * \
          math.sin(self.angle + self.angular_speed * t + self.angular_acel * t * t / 2) + \
          (self.line_speed + self.line_acel * t) * math.cos(self.angle) * \
          math.cos(self.angle + self.angular_speed * t + self.angular_acel * t * t / 2)
    self.line_speed = math.sqrt(v_x * v_x + v_y * v_y)
    self.angle += self.angular_speed * t + self.angular_acel * t * t / 2
    self.angular_speed = angle_v
    x =
    y =
    v_x = (self.line_speed + self.line_acel * (t_ - t)) * math.cos(self.angle) * \
          math.cos(self.angle + self.angular_speed * (t_ - t)) - \
          (self.line_speed + self.line_acel * (t_ - t)) * math.sin(self.angle) * \
          math.sin(self.angle + self.angular_speed * (t_ - t))
    v_y = (self.line_speed + self.line_acel * (t_ - t)) * math.sin(self.angle) * \
          math.sin(self.angle + self.angular_speed * (t_ - t)) + \
          (self.line_speed + self.line_acel * (t_ - t)) * math.cos(self.angle) * \
          math.cos(self.angle + self.angular_speed * (t_ - t))
    self.line_speed = math.sqrt(v_x * v_x + v_y * v_y)
    self.angle += self.angular_speed * (t_ - t)
    x +=
    y +=
    v_x = (self.line_speed) * math.cos(self.angle) * math.cos(self.angle + self.angular_speed * (self.T - t_)) - \
          (self.line_speed) * math.sin(self.angle) * math.sin(self.angle + self.angular_speed * (self.T - t_))
    v_y = (self.line_speed) * math.sin(self.angle) * math.sin(self.angle + self.angular_speed * (self.T - t_)) + \
          (self.line_speed) * math.cos(self.angle) * math.cos(self.angle + self.angular_speed * (self.T - t_))
    self.line_speed = l_v
    self.angle += self.angular_speed * (self.T - t_)
    x +=
    y +=
else:
    v_x = (self.line_speed + self.line_acel * t_) * math.cos(self.angle) * \
          math.cos(self.angle + self.angular_speed * t + self.angular_acel * t_ * t_ / 2) - \
          (self.line_speed + self.line_acel * t_) * math.sin(self.angle) * \
          math.sin(self.angle + self.angular_speed * t_ + self.angular_acel * t_ * t_ / 2)

    v_y = (self.line_speed + self.line_acel * t_) * math.sin(self.angle) * \
          math.sin(self.angle + self.angular_speed * t_ + self.angular_acel * t_ * t_ / 2) + \
          (self.line_speed + self.line_acel * t_) * math.cos(self.angle) * \
          math.cos(self.angle + self.angular_speed * t_ + self.angular_acel * t_ * t_ / 2)
    self.line_speed = l_v
    self.angle += self.angular_speed * t_ + self.angular_acel * t_ * t_ / 2
    self.angular_speed += self.angular_acel * t_
    x =
    y =
    v_x = (self.line_speed) * math.cos(self.angle) * \
          math.cos(self.angle + self.angular_speed * (t - t_)) - \
          (self.line_speed) * math.sin(self.angle) * \
          math.sin(self.angle + self.angular_speed * (t - t_))
    v_y = (self.line_speed) * math.sin(self.angle) * \
          math.sin(self.angle + self.angular_speed * (t - t_)) + \
          (self.line_speed) * math.cos(self.angle) * \
          math.cos(self.angle + self.angular_speed * (t - t_))
    self.angle += self.angular_speed * (t - t_) + self.angular_acel * (t - t_) * (t - t_) / 2
    self.angular_speed = angle_v
    x +=
    y +=
    v_x = (self.line_speed) * math.cos(self.angle) * math.cos(self.angle + self.angular_speed * (self.T - t)) - \
          (self.line_speed) * math.sin(self.angle) * math.sin(self.angle + self.angular_speed * (self.T - t))
    v_y = (self.line_speed) * math.sin(self.angle) * math.sin(self.angle + self.angular_speed * (self.T - t)) + \
          (self.line_speed) * math.cos(self.angle) * math.cos(self.angle + self.angular_speed * (self.T - t))
    self.angle += self.angular_speed * (self.T - t_)
    x +=
    y +=
self.x = x
self.y = y
self.covered_area()  # 修改顶点坐标