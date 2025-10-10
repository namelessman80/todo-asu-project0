import axios from "axios";
import type {
  User,
  Task,
  TaskCreate,
  TaskUpdate,
  Label,
  LabelCreate,
  UserSignup,
  UserLogin,
  AuthResponse,
} from "@/types";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api";

// Create axios instance with base configuration
const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// Add token to requests if available
api.interceptors.request.use((config) => {
  if (typeof window !== "undefined") {
    const token = localStorage.getItem("token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
  }
  return config;
});

// Auth API
export const authAPI = {
  signup: async (data: UserSignup): Promise<User> => {
    const response = await api.post<User>("/auth/signup", data);
    return response.data;
  },

  login: async (data: UserLogin): Promise<AuthResponse> => {
    const formData = new URLSearchParams();
    formData.append("username", data.username);
    formData.append("password", data.password);

    const response = await api.post<AuthResponse>("/auth/login", formData, {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    });
    return response.data;
  },

  logout: async (): Promise<{ message: string }> => {
    const response = await api.post<{ message: string }>("/auth/logout");
    return response.data;
  },

  getCurrentUser: async (): Promise<User> => {
    const response = await api.get<User>("/users/me");
    return response.data;
  },
};

// Tasks API
export const tasksAPI = {
  getAll: async (label?: string, completed?: boolean): Promise<Task[]> => {
    const params: any = {};
    if (label) params.label = label;
    if (completed !== undefined) params.completed = completed;
    const response = await api.get<Task[]>("/tasks", { params });
    return response.data;
  },

  getById: async (id: string): Promise<Task> => {
    const response = await api.get<Task>(`/tasks/${id}`);
    return response.data;
  },

  create: async (data: TaskCreate): Promise<Task> => {
    const response = await api.post<Task>("/tasks", data);
    return response.data;
  },

  update: async (id: string, data: TaskUpdate): Promise<Task> => {
    const response = await api.put<Task>(`/tasks/${id}`, data);
    return response.data;
  },

  delete: async (id: string): Promise<void> => {
    await api.delete(`/tasks/${id}`);
  },
};

// Labels API
export const labelsAPI = {
  getAll: async (): Promise<Label[]> => {
    const response = await api.get<Label[]>("/labels");
    return response.data;
  },

  getById: async (id: string): Promise<Label> => {
    const response = await api.get<Label>(`/labels/${id}`);
    return response.data;
  },

  create: async (data: LabelCreate): Promise<Label> => {
    const response = await api.post<Label>("/labels", data);
    return response.data;
  },

  update: async (
    id: string,
    data: Partial<LabelCreate>
  ): Promise<Label> => {
    const response = await api.put<Label>(`/labels/${id}`, data);
    return response.data;
  },

  delete: async (id: string): Promise<void> => {
    await api.delete(`/labels/${id}`);
  },
};

export default api;
