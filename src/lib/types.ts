import type { Database } from './supabase.ts'

export type Matchup = {
    leader1: Leader
    leader2: Leader
}

export type Leader = Database['public']['Tables']['leaders']['Row']