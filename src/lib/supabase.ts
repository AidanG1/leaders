export type Json =
  | string
  | number
  | boolean
  | null
  | { [key: string]: Json | undefined }
  | Json[]

export interface Database {
  public: {
    Tables: {
      leader_states: {
        Row: {
          created_at: string
          id: string
          leader_link: string
          state_link: string
        }
        Insert: {
          created_at?: string
          id?: string
          leader_link: string
          state_link: string
        }
        Update: {
          created_at?: string
          id?: string
          leader_link?: string
          state_link?: string
        }
        Relationships: [
          {
            foreignKeyName: "leader_states_leader_link_fkey"
            columns: ["leader_link"]
            isOneToOne: false
            referencedRelation: "leaders"
            referencedColumns: ["wikipedia_link"]
          },
          {
            foreignKeyName: "leader_states_state_link_fkey"
            columns: ["state_link"]
            isOneToOne: false
            referencedRelation: "states"
            referencedColumns: ["wikipedia_link"]
          }
        ]
      }
      leaders: {
        Row: {
          active: boolean
          created_at: string
          id: string
          image_url: string
          name: string
          title: string
          wikipedia_link: string
        }
        Insert: {
          active?: boolean
          created_at?: string
          id?: string
          image_url: string
          name: string
          title: string
          wikipedia_link: string
        }
        Update: {
          active?: boolean
          created_at?: string
          id?: string
          image_url?: string
          name?: string
          title?: string
          wikipedia_link?: string
        }
        Relationships: []
      }
      states: {
        Row: {
          created_at: string
          flag_url: string | null
          id: string
          name: string | null
          wikipedia_link: string
        }
        Insert: {
          created_at?: string
          flag_url?: string | null
          id?: string
          name?: string | null
          wikipedia_link: string
        }
        Update: {
          created_at?: string
          flag_url?: string | null
          id?: string
          name?: string | null
          wikipedia_link?: string
        }
        Relationships: []
      }
      votes: {
        Row: {
          created_at: string
          id: string
          loser: string
          winner: string
        }
        Insert: {
          created_at?: string
          id?: string
          loser: string
          winner: string
        }
        Update: {
          created_at?: string
          id?: string
          loser?: string
          winner?: string
        }
        Relationships: [
          {
            foreignKeyName: "votes_loser_fkey"
            columns: ["loser"]
            isOneToOne: false
            referencedRelation: "leaders"
            referencedColumns: ["id"]
          },
          {
            foreignKeyName: "votes_winner_fkey"
            columns: ["winner"]
            isOneToOne: false
            referencedRelation: "leaders"
            referencedColumns: ["id"]
          }
        ]
      }
    }
    Views: {
      [_ in never]: never
    }
    Functions: {
      leaderboard: {
        Args: Record<PropertyKey, never>
        Returns: {
          leader_name: string
          image_url: string
          wikipedia_link: string
          total_wins: number
          total_losses: number
          win_percentage: number
        }[]
      }
    }
    Enums: {
      [_ in never]: never
    }
    CompositeTypes: {
      [_ in never]: never
    }
  }
}

export type Tables<
  PublicTableNameOrOptions extends
    | keyof (Database["public"]["Tables"] & Database["public"]["Views"])
    | { schema: keyof Database },
  TableName extends PublicTableNameOrOptions extends { schema: keyof Database }
    ? keyof (Database[PublicTableNameOrOptions["schema"]]["Tables"] &
        Database[PublicTableNameOrOptions["schema"]]["Views"])
    : never = never
> = PublicTableNameOrOptions extends { schema: keyof Database }
  ? (Database[PublicTableNameOrOptions["schema"]]["Tables"] &
      Database[PublicTableNameOrOptions["schema"]]["Views"])[TableName] extends {
      Row: infer R
    }
    ? R
    : never
  : PublicTableNameOrOptions extends keyof (Database["public"]["Tables"] &
      Database["public"]["Views"])
  ? (Database["public"]["Tables"] &
      Database["public"]["Views"])[PublicTableNameOrOptions] extends {
      Row: infer R
    }
    ? R
    : never
  : never

export type TablesInsert<
  PublicTableNameOrOptions extends
    | keyof Database["public"]["Tables"]
    | { schema: keyof Database },
  TableName extends PublicTableNameOrOptions extends { schema: keyof Database }
    ? keyof Database[PublicTableNameOrOptions["schema"]]["Tables"]
    : never = never
> = PublicTableNameOrOptions extends { schema: keyof Database }
  ? Database[PublicTableNameOrOptions["schema"]]["Tables"][TableName] extends {
      Insert: infer I
    }
    ? I
    : never
  : PublicTableNameOrOptions extends keyof Database["public"]["Tables"]
  ? Database["public"]["Tables"][PublicTableNameOrOptions] extends {
      Insert: infer I
    }
    ? I
    : never
  : never

export type TablesUpdate<
  PublicTableNameOrOptions extends
    | keyof Database["public"]["Tables"]
    | { schema: keyof Database },
  TableName extends PublicTableNameOrOptions extends { schema: keyof Database }
    ? keyof Database[PublicTableNameOrOptions["schema"]]["Tables"]
    : never = never
> = PublicTableNameOrOptions extends { schema: keyof Database }
  ? Database[PublicTableNameOrOptions["schema"]]["Tables"][TableName] extends {
      Update: infer U
    }
    ? U
    : never
  : PublicTableNameOrOptions extends keyof Database["public"]["Tables"]
  ? Database["public"]["Tables"][PublicTableNameOrOptions] extends {
      Update: infer U
    }
    ? U
    : never
  : never

export type Enums<
  PublicEnumNameOrOptions extends
    | keyof Database["public"]["Enums"]
    | { schema: keyof Database },
  EnumName extends PublicEnumNameOrOptions extends { schema: keyof Database }
    ? keyof Database[PublicEnumNameOrOptions["schema"]]["Enums"]
    : never = never
> = PublicEnumNameOrOptions extends { schema: keyof Database }
  ? Database[PublicEnumNameOrOptions["schema"]]["Enums"][EnumName]
  : PublicEnumNameOrOptions extends keyof Database["public"]["Enums"]
  ? Database["public"]["Enums"][PublicEnumNameOrOptions]
  : never
