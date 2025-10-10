export interface User {
  id: string;
  email: string;
  full_name?: string;
  created_at: string;
}

export interface Task {
  id: string;
  title: string;
  description?: string;
  priority: "High" | "Medium" | "Low";
  deadline: string;
  completed: boolean;
  labels: string[];
  user_id: string;
  created_at: string;
  updated_at: string;
}

export interface Label {
  id: string;
  name: string;
  color: string;
  user_id: string;
  created_at: string;
}

export interface TaskCreate {
  title: string;
  description?: string;
  priority: "High" | "Medium" | "Low";
  deadline: string;
  completed?: boolean;
  labels?: string[];
}

export interface TaskUpdate {
  title?: string;
  description?: string;
  priority?: "High" | "Medium" | "Low";
  deadline?: string;
  completed?: boolean;
  labels?: string[];
}

export interface LabelCreate {
  name: string;
  color?: string;
}

export interface UserSignup {
  email: string;
  password: string;
  full_name?: string;
}

export interface UserLogin {
  username: string;
  password: string;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
}






